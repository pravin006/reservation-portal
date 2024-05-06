from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models.course import COURSES
from models.bookings import BOOKINGS
import json
from datetime import datetime, timedelta, date
from models.chart import CHART

chartdashboard = Blueprint('chartdashboard', __name__)

@chartdashboard.route('/chartdashboard', methods=['GET','POST'])
@login_required
def render_chartdashboard():
    if request.method == 'GET':
        # edit
        email = request.args.get('user')
        if email:
            existing_course = []
            # email = email.strip("'")
            existing_bookings = BOOKINGS.objects(user=current_user)
            for b in existing_bookings:
                existing_course.append(b.courseName.course)
            panel = "View Booking"
        # end
        else:
            existing_course = COURSES.objects.distinct( "course")
            panel = "Dashboard"
        return render_template('chartdashboard.html', panel= panel, courses = existing_course)

    elif request.method == 'POST':

        name = request.form['name']
        user_or_all = request.form['type']
        # print(user_or_all)
        existing_course = COURSES.objects(course=name).first()
        # edit
        holes = existing_course['holes']
        # end
        if user_or_all == 'View Booking':
            existing_booking = BOOKINGS.objects(courseName = existing_course, user = current_user).first()
        else:
            existing_booking = BOOKINGS.objects(courseName = existing_course)
            # existing_booking_list = []
            # for i in existing_booking:
            #     existing_booking_list += i['date']
            # print(existing_booking_list)
    

        if existing_booking:
            CHART.objects().delete()
            a_chart = CHART(labels=None, charts=None).save()
            
            if user_or_all == 'View Booking':
                dates_list = existing_booking['date']
                # a_chart.new_collection(dates_list, holes)
            else:
                # print(existing_booking)
                # for i in existing_booking:
                #     dates_list = i['date']
                dates_list = []
                for i in existing_booking:
                    dates_list += i['date']
            a_chart.new_collection(dates_list, holes)

            # dates_list = existing_booking['date']
            # print('Here')
            # print(type(dates_list))

            # CHART.objects().delete()

            # # create a chart obj with None values
            # a_chart = CHART(labels=None, charts=None).save()
            # # a_chart.new_collection(dates_list, index, par, dist)

            


            # # edit
            # a_chart.new_collection(dates_list, holes)
            # end


            existing_chart = CHART.objects().all()
            label = existing_chart[0]['labels']
            chart = existing_chart[0]['charts']

        else:
            chart = []
            label = []

    return jsonify({'charts':chart, 'labels':label})
