# FoodTrucks
**Code Background**

This code is a solution to the Take Home Engineering Challenge which is presented here.

https://github.com/timfpark/take-home-engineering-challenge

**Instructions:**

For this problem, you must install the following Python modules:

Flask, pandas, and wtforms

To run this solution, index to the overarching directory and entering the following commands from the command line:

set FLASK_APP = market

flask run

**Overview:**

This solution makes use of five seperate files which are all used to meet the requirements of the problem.

Food_Truck.py is the python file which handles the server routing betweeen subpages and calls functions dependent on the page you are on.

User_Input.py is the python file which wtforms is used to enter desired coordinates and then compare them with the csv files which have been pulled via pandas.  The output of the main class of this file is a list of dictionaries which is used to handle the final output.

base.html is an html file which is being used as the main template for all other html files to pull information from.

home.html is an html file which is specific to the home page and uses JINJA2 to collect form data from the user and pass it into the main class in User_Input.py.

fooddata.html is an html file which is specific to the sub page which shows a list of food trucks closest to the coordinates entered.  It makes use of JINJA2 to pass through the list of dictionaries that is outputted from User_Input.py

**Design Choices:**

When designing this solution I had to make multiple decisions which affected the overall product of the code.

The first choice I made was to use Python Flask for this solution.  I have been recently learning and practicing Python so I saw this as a good opportunity to put my backend skills to the test.  Additionally I wanted to learn something new through solving this problem and that's where Python Flask comes in.  It allowed me to learn how to use the micro-framework to handle http requests and route information to html.

Another choice I made when designing this problem was how to pass data from one subpage to another.  I used flask sessions to pass the data between pages.  My original plan was to use a class for foodtruck with attributes 'Applicant' and 'Address', then return from the class a list of foodtruck objects.  When I tried to pass this data using sessions it did not go through since the objects were not serializable for JSON.  Instead I changed the design to pass through a list of key - value pair dictionaries which was able to pass through just fine.

**Future Optimizations**

If I had more time to work on this project there are a few changes that I would like to make.  

Ideally I would've made the html and css of the pages would look cleaner and more professional including how the form is presented on the home page.  

I would also have liked to allow specific filters based on the food items which is data available in the CSV fil, and this data could limit the outputted data with food trucks that have one of the items specified.  

The final change I would've like  to have made would be to clean up the outputted table and allow for each food truck to be selected and link to Google Maps per the longitude and latitude of that food truck.

**Personal Growth:**

In order to tackle this problem, I needed to go quite a bit out of my comfort zone.  

I had never before done full stack development on my own nor had I needed to set up all the environments on my own to run a localhost.  

The way I addressed this problem required me to do both of these tasks.  

Additonally, this was my first problem in which I used Flask, wtforms, or pandas.  

I have been learning Python for the last 2 months and this allowed me to comfortably execute what I've learned within the document User_Input.py.  

Finally, this project has been a reintroduction to HTML for me which I had not used since a few years ago.

Overall, I'm very happy with what I've been able to learn from this project and look forward to applying this knowledge elsewhere.
