import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

@app.route('/')
def list_schools():
    schools = School.query.all()
    return render_template('schools.html', schools=schools)

@app.route('/school/<sid>')
def view_school(sid):
    school = School.query.get(sid)
    if not school:
        return "No such school"
    teachers = school.teachers
    return render_template('view_school.html', school=school, teachers=teachers)

@app.route('/teacher/<tid>')
def view_teacher(tid):
    teach = Teacher.query.get(tid)
    if not teach:
        return "No such teacher"
    quotes = teach.quotes
    return render_template('view_teacher.html', quotes=teach.quotes, teacher=teach)

if __name__ == '__main__':
    app.run()