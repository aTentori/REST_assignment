import json
import os
import sqlite3

# used to wrap everything into a format
from db_utility import *


def dictionary_factory(cursor, row):
    column_names = [d[0].lower() for d in cursor.description]
    return dict(zip(column_names, row))


def get_all_areas():
    """
    Returns a list of dictionaries representing all the rows in the
    area table.
    """
    # connect to database python library
    conn = sqlite3.connect("measures.sqlite")
    # create cursor
    cursor = conn.cursor()
    # sql statement
    cursor.execute("select * from area")

    rows = cursor.fetchall()
    # closes connection to database
    conn.close()

    return rows


def get_locations_for_area(area_id):
    """
    Return a list of dictionaries giving the locations for the given area.
    """
    conn = sqlite3.connect("measures.sqlite")

    cursor = conn.cursor()
    # select all from location and specifically get the location location area
    # ? puts area_id in place of the question mark
    cursor.execute("select * from location where location.location_area = ? ", (area_id,))

    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:

        result.append(dictionary_factory(cursor,row))

    return result

def get_measurements_for_location(location_id):
    """
    Return a list of dictionaries giving the measurement rows for the given location.
    """

    conn = sqlite3.connect("measures.sqlite")

    cursor = conn.cursor()

    cursor.execute("select * from measurement where measurement_location = ? ", (location_id,))

    rows = cursor.fetchall()
    conn.close()

    result = []

    for row in rows:
        result.append(dictionary_factory(cursor, row))

    return result


def get_categories_for_area(area_id):
    """
    Return a list of rows from the category table that all contain the given area.
    """
    conn = sqlite3.connect("measures.sqlite")

    cursor = conn.cursor()
    cursor.execute("select * "
                   "from category c "
                   "left outer join category_area ca "
                   "on  c.category_id = ca.category_id "
                   "where ca.area_id = ? ", (area_id,))

    rows = cursor.fetchall()
    conn.close()

    result = []

    for row in rows:
        result.append(dictionary_factory(cursor, row))

    return result


def get_report():
    """
    retrieves data report
    :return: necessary report
    """
    report = []

    areas = get_all_areas()

    for area in areas:
        num_loc = number_of_locations_by_area(area[0])
        avg_val = get_average_measurements_for_area(area[0])
        categories = get_categories_for_area(area[0])

        if num_loc is None:
            num_loc = 0

        if avg_val is None:
            avg_val = "----------"
        else:
            avg_val = round(avg_val, 2)

        cat_str = ""
        for category in categories:
            cat_str += category['name'] + ", "
        cat_str = cat_str[:-2]

        report.append(
            (
                area[0],
                area[1],
                num_loc,
                avg_val,
                cat_str
            )
        )

    return report
