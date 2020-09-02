import requests
from bottle import route, run, template, static_file

from db_access import get_report


@route('/')
def web_report():
    report = get_report()
    return template('report.html', report=report)


@route('/web.css')
def stylesheets():
    return static_file('web.css', root='.')


run(host='localhost', port=8085)
