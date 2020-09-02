import requests
from bottle import route, run, template, static_file

from db_access import *


@route('/')
def web_report():
    report = []

    areas = get_all_areas()

    print(areas)

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

    return template('report.html', report=report)


@route('/web.css')
def stylesheets():
    return static_file('web.css', root='.')

# list one folder
# Part B of Notes project
# provide the function that will display a single folder
# the template is 'folder.html'
# use REST requests to get the needed data
# check the template for the key words used to name the data
# check for errors in the id, see the 'note' route above for guidance
@route('/folder')
def get_folder():
    folder_id = request.query['folder_id']
    folder = requests.get("http://localhost:21212/folder/" + folder_id).json()
    notes_in_folder = requests.get("http://localhost:21212/folder/notes/" + folder_id).json()
    return template("folder.html", folder=folder, notes=notes_in_folder)



run(host='localhost', port=8085)
