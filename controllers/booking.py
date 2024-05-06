from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models.course import COURSES
import json

booking = Blueprint('booking', __name__)

@booking.route('/booking', methods=['GET','POST'])
@login_required
def render_booking():
    if request.method == 'POST':
        # it gets the value which is "item.course" from an element named "which_type"
        typ = request.form.get('submit_button')
        existing_course = COURSES.objects(course=typ).first()
        # print(type(existing_course))
        return render_template('booking.html', courses = existing_course, name=current_user.name, panel = existing_course.course)