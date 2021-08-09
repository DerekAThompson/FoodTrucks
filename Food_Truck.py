from flask import Flask, render_template, redirect, session
from User_Input import UserLocation

app = Flask(__name__)
app.config['SECRET_KEY'] = '8aa1d5c1be13720989738952'

# Home Page which requests coordinates
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def food_truck():
    form = UserLocation()
    if form.validate_on_submit():
        session['userCoords'] = form.compare()
        return redirect('/food_data')
    return render_template('home.html', form = form)  

# fooddata sub page which displays food options
@app.route('/food_data', methods = ['GET', 'POST'])
def food_data():
    userCoords = session['userCoords']
    return render_template('fooddata.html', userCoords = userCoords)

if __name__ == '__main__':
    app.run(debug=True)


