from json import dumps

from bottle import route, run

from db_access import get_report


@route("/report")
def report():
    return dumps(get_report())


run(host='localhost', port=21212)
