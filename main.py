from flask import Flask, render_template  # pip install flask
import datetime
import psutil  # pip install psutil

app = Flask(__name__)


@app.route('/') # main page
@app.route('/index')
def index():
    current_time = datetime.datetime.now()
    data = {
        "hour" : current_time.hour,
        "minute" : current_time.minute,
        "second" : current_time.second,
        "year" : current_time.year,
        "month" : current_time.month,
        "day" : current_time.day,
        "battery" : psutil.sensors_battery().percent
    }
    return render_template('index.html', **data)


app.run(port=8080, host='127.0.0.1')