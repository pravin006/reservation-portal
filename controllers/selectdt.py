from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models.course import COURSES
from models.bookings import BOOKINGS
from datetime import datetime
import json

selectdt = Blueprint('selectdt', __name__)

@selectdt.route('/selectdt', methods=['GET','POST'])
@login_required
def render_selectdt():
    # if request.method == 'POST':
    #     typ = request.form.get('birthdaytime')
    #     print(typ)
    dt = request.form['dt']
    name = request.form['name']
    print(type(dt), name)
    existing_course = COURSES.objects(course=name).first()
    userCourseRec = BOOKINGS.objects(user=current_user, courseName = existing_course).first()
    dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M')
    if userCourseRec:
        listOfDates = userCourseRec.date
        listOfDates.append(dt)
        userCourseRec.update(__raw__={'$set': {'date': listOfDates}})
    else:
        a_booking = BOOKINGS(date=[dt],user=current_user,courseName=existing_course).save()
    return jsonify({'dt' : dt})
    