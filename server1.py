from bottle import route, run, template 
from db_access import *
from db_utility import *
from json import *


@route('/areas')  # path =  /areas
def areas():  # function = area()
    return dumps(get_all_areas()) # this is actual function for this case


@route('/area/<area_id>/locations')
def location_by_area(area_id):
    return dumps(get_locations_for_area(area_id=area_id))


@route('/location/<location_id>/measurements')
def measurements_by_location(location_id):
    return dumps(get_measurements_for_location(location_id))


@route('/area/<area_id>/categories')
def categories_by_area(area_id):
    return dumps(get_categories_for_area(area_id))


@route('/area/<area_id>/average_measurement')
def average_measure_by_area(area_id):
    return dumps(get_average_measurements_for_area(area_id))


@route('/area/<area_id>/number_locations')
def number_locations_by_area(area_id):
    return dumps(number_of_locations_by_area(area_id))


run(host='localhost', port=21212)
