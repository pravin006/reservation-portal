from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from flask import flash
import csv
import io #reading file
from models.bookings import BOOKINGS
from models.course import COURSES
from models.users import User
from models.holes import HOLE
import ast
from datetime import datetime

upload = Blueprint('upload', __name__)


@upload.route("/upload", methods=['GET','POST'])
@login_required
def render_upload():
    # if hte user just key in the /upload in the address
    if request.method == 'GET':
        return render_template("upload.html", name=current_user.name, panel="Upload")
    elif request.method == 'POST':
        # type variable is found from html <input name="type" type="hidden" value="upload">
        # it gets the value which is "upload" from an element named "type"
        type = request.form.get('type')
        # <input class="upload" id='upload' name='file' type='file' accept='.csv' required>
        # get csv object from front end with the name "file"
        file = request.files.get('file')       
        # read the csv object and decode the characters
        data = file.read().decode('utf-8')
        dict_reader = csv.DictReader(io.StringIO(data), delimiter=',', quotechar='"') #quotechar='"' adds quotes to each str
        file.close()

        options = request.form.get('filetype')
        # selected = options.value
        
        # if type == 'create':
        #     print("No create Action yet")
        if type == 'upload':
            try:
                if options == 'courses':
                    # loop through the dict and create a course obj for each line and save to db
                    for item in list(dict_reader):
                        course = item['course']
                        ind = ast.literal_eval(item['index'])
                        par = ast.literal_eval(item['par'])
                        dist = ast.literal_eval(item['dist'])
                        image_url = item['image_url'] 
                        description = item['description']
                        # edit
                        existing_course = COURSES.objects(course=course).first()
                        if existing_course == None:
                            holes_list = []
                            for i in range(len(ind)):
                                new_hole = HOLE(index = ind[i], par = par[i], dist = dist[i]).save()
                                holes_list.append(new_hole)
                            
                            a_course = COURSES(course=course,holes = holes_list, image_url=image_url,description=description).save()
                        # end

                        # existing_course = COURSES.objects(course=course).first()
                        # print(existing_course)
                        # if existing_course == None:
                        #     a_course = COURSES(course=course,index=ind,par=par,dist=dist, image_url=image_url,description=description).save()
                        
                        

                else:
                    for item in list(dict_reader):
                        #check if the user_email is actually in db using the user email from the csv. gives a user obj or none
                        existing_user = User.objects(email=item['user']).first()
                        existing_course = COURSES.objects(course=item['course_name']).first()
                        if existing_user and existing_course:
                            userCourseRec = BOOKINGS.objects(user=existing_user, courseName = existing_course).first()
                            date_time = item['check_in_time']
                            date_time = datetime.strptime(date_time, '"%d/%m/%Y %I:%M:%S %p"')
                            if userCourseRec:
                                listOfDates = userCourseRec.date
                                # print(listOfDates)
                                listOfDates.append(date_time)
                                print(listOfDates)
                                userCourseRec.update(__raw__={'$set': {'date': listOfDates}})
                            else:
                                course_name = item['course_name']
                                date_time = [date_time]
                                a_booking = BOOKINGS(date=date_time,user=existing_user,courseName=existing_course).save()
                flash('Upload successful!', 'success')
            except Exception as e:
                flash(f'Upload failed: {e}', 'danger')

        return render_template("upload.html", name=current_user.name, panel="Upload")
