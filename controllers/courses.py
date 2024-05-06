from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models.course import COURSES
import json

courses = Blueprint('courses', __name__)

@courses.route('/courses', methods=['GET','POST'])
@login_required
def render_courses():
    if request.method == 'GET':
        existing_courses = COURSES.objects().all()
        # json_data = existing_courses.to_json()
        course_list = json.loads(existing_courses.to_json())
        # for i in lis:
        #     print(i['course'])
        return render_template('courses.html', courses = course_list, name=current_user.name, panel = 'Course')
