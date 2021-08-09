# FoodTrucks
For this problem, you must install the following Python modules:
Flask, pandas, and wtforms

To run this solution, index to the overarching directory and entering the following commands from the command line:
set FLASK_APP = market
flask run

This solution makes use of five seperate files which are all used to meet the requirements of the problem.
Food_Truck.py is the python file which handles the server routing betweeen subpages and calls functions dependent on the page you are on.
User_Input.py is the python file which wtforms is used to enter desired coordinates and then compare them with the csv files which have been pulled via pandas.  The output of the main class of this file is a list of dictionaries which is used to handle the final output.
base.html is an html file which is being used as the main template for all other html files to pull information from.
home.html is an html file which is specific to the home page and uses JINJA2 to collect form data from the user and pass it into the main class in User_Input.py.
fooddata.html is an html file which is specific to the sub page which shows a list of food trucks closest to the coordinates entered.  It makes use of JINJA2 to pass through the list of dictionaries that is outputted from User_Input.py

In order to tackle this problem, I needed to go quite a bit out of my comfort zone.  I had never before done full stack development on my own nor had I needed to set up all the environments on my own to run a localhost.  The way I addressed this problem required me to do both of these tasks.  Additonally, this was my first problem in which I used Flask, wtforms, or pandas.  I have been learning Python for the last 2 months and this allowed me to comfortably execute what I've learned within the document User_Input.py.  Finally, this project has been a reintroduction to HTML for me which I had not used since a few years ago.

Overall, I'm very happy with what I've been able to learn from this project and look forward to applying this knowledge elsewhere.
