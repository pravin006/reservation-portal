# from flask import render_template, request, jsonify, Blueprint
# import math
# from datetime import datetime,date,timedelta

# from flask_login import login_required, current_user

# from models.bmidaily import BMIDAILY
# from models.bmilog import COURSES
# from models.users import User


# # We need to initilize the blueprint for bmi
# bmi = Blueprint('bmi', __name__)



# # Using Back-end for calculation
# @bmi.route("/process", methods=['GET','POST'])
# @login_required
# def process():
#     #get the weight and height and uom from the form and the custom.js
#     weight  = float(request.form['weight'])
#     height = float(request.form['height'])

#     # Since there is only one reading allowed in each day, the latest will be the log
#     today = date.today()
#     now = datetime.now()
    
#     #get the current user object first. User object or None
#     existing_user = User.objects(email=current_user.email).first()
    
#     if existing_user:
#         #create a new document in the BMILog Collection
#         bmilogObject = COURSES(user=existing_user, datetime=now, weight=weight, height=height)
#         #compute the bmi for the newly created BMILog object and store in its bmi var
#         bmilogObject.bmi = bmilogObject.computeBMI(request.form['unit']) #m or cm
#         #save the BMILog object to db
#         bmilogObject.save()

#         #getting a BMIDaily object which is for the current user object var defined and date. 
#         #Either one obj or Can be None if logging for the first time for the day and user
#         bmidailyObjects = BMIDAILY.objects(user=existing_user, date=today) #GET INFO
        
#         #if there is already a record before for the day
#         if len(bmidailyObjects) >= 1:
#             #update the existing document
#             #call the updatedBMI() method to calculate the new avg bmi
#             new_bmi_average = bmidailyObjects[0].updatedBMI(bmilogObject.bmi) #[0] is because it is for the one and only record
#             #get the number of times bmi has been update for the day already
#             number = bmidailyObjects[0].numberOfMeasures
#             #update the bmiDaily collection in the db by increasing the count by 1 and setting the new avgbmi
#             bmidailyObjects[0].update(__raw__={'$set': {'numberOfMeasures': number + 1, 'averageBMI': new_bmi_average}})
#         #if there is no log today for the user
#         else:
#             #make a new  bmiDaily object. default count is 1
#             bmidailyObject = BMIDAILY(user=existing_user, date=today, numberOfMeasures=1, averageBMI = bmilogObject.bmi)
#             #save the object in the db
#             bmidailyObject.save()
#     # bmi is returned back to custom.js            
#     return jsonify({'bmi' : bmilogObject.bmi})


#     # if request.method == 'GET':
#     #     return render_template('log.html')

#     # elif request.method == 'POST':
#     #     weight  = float(request.form['weight'])
#     #     height = float(request.form['height'])
#     #     unit = request.form['unit']

#     #     if unit == 'm':
#     #         bmi = weight / math.pow(height, 2)
#     #     else:
#     #         bmi = weight / math.pow(height/100, 2)

#     #     print('BMI: {}'.format(bmi))
#     #     return jsonify({'bmi' : bmi})   # Convert to Json format and response back to the Ajax method