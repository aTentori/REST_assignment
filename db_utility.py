import os
import sqlite3


def dictionary_factory(cursor, row):
    column_names = [d[0].lower() for d in cursor.description]
    return dict(zip(column_names, row))


def get_average_measurements_for_area(area_id):
    """
    Returns the average value of all measurements for all locations in the given area.
    Returns None if there are no measurements.
    """
    conn = sqlite3.connect("measures.sqlite")

    cursor = conn.cursor()
    # avg is to get average of values from measurement join to get the matching ids from measurement and location
    cursor.execute("select avg(value) "
                   "from measurement "
                   "left outer join location "
                   "on measurement.measurement_location = location.location_id "
                   "where location.location_area = ?  ", (area_id,))

    row = cursor.fetchall()
    conn.close()

    print(row[0])
    # two dimensional array to print rows and columns
    if row[0][0]:
        return float(row[0][0])
    else:
        return None



def number_of_locations_by_area(area_id):
    """
    Returns the number of locations for the given area.
    """
    conn = sqlite3.connect("measures.sqlite")

    cursor = conn.cursor()
    cursor.execute("select count(*) "
                   "from location "
                   "where location.location_area = ?  ", (area_id,))

    row = cursor.fetchall()
    conn.close()
    if row[0][0]:
        return float(row[0][0])
    else:
        return None


