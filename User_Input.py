from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange
import pandas
import math

# Class which accepts user input for the desired Longitude and Latitude
class UserLocation(FlaskForm):
    latitude = DecimalField('Latitude', validators = [NumberRange(min = -90, max = 90, message = 'must be a number between -90 and 90 (e.g. 37.792252)'), InputRequired(message = 'must be a number between -90 and 90 (e.g. 37.792252)')])
    longitude = DecimalField('Longitude', validators = [NumberRange(min = -180, max = 180, message = 'must be a number between -180 and 180 (e.g. -122.403793)'), InputRequired(message = 'must be a number between -180 and 180 (e.g. -122.403793)')])
    submit = SubmitField('Find Food Trucks')

    def compare(self):
        #Gets user data
        userLatitude = self.latitude.data
        userLongitude = self.longitude.data

        # Pulls CSV file
        url = 'https://data.sfgov.org/api/views/rqzj-sfat/rows.csv'
        foodTruckData = pandas.read_csv(url)

        # Creates a list to which calculated distance will be stored
        calcDist = []

        # Indexes through each entry in the CSV file
        for index in foodTruckData.index:
            # Pulls longitude, latitude
            latitude = float(foodTruckData['Latitude'][index])
            longitude = float(foodTruckData['Longitude'][index])

            # Checks to see if latitude or longitude is empty and if so assigns Null to calculated distance
            if latitude == 0 or longitude == 0:
                calcDist.append('Null')

            else:
                # Performs Pythagorean Theorem to gauge distance and adds to calculated distance list
                a = abs(float(userLatitude)) - abs(latitude)
                b = abs(float(userLongitude)) - abs(longitude)
                distance = math.sqrt((a ** 2) + (b ** 2))
                calcDist.append(str(distance))

        # Makes foodTruckDatanew dataframe which contains the calculated distance as a column
        foodTruckData = foodTruckData.assign(distance = calcDist)

        # Sorts food truck data by distance
        foodTruckData = foodTruckData.sort_values(by = ['distance'], ignore_index = True)

        # Creates list and appends desired number of food trucks closest food trucks as FoodTruck object containing applicant and address variable
        numFoodTrucks = 5
        closeFoodTrucks = [0] * numFoodTrucks
        for index in range(numFoodTrucks):
            closeFoodTrucks[index] = {foodTruckData['Address'][index] : foodTruckData['Applicant'][index]}
        return closeFoodTrucks