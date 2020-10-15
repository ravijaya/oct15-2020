from flask import Flask, render_template
from time import ctime
from os import environ

app = Flask(__name__)


@app.route('/env')
def print_env():
    return render_template('env.html', environ=environ, title='Environment variable')

@app.route('/ts')
def timestamp():
    ts = ctime()
    return render_template('ts.html', ts=ts, title='current server time')


@app.route('/')
def home_page():
    greetings = 'a sample application'
    return render_template('index.html', mesg=greetings, title="a sample flask app")


# http://127.0.0.1:5000/ts

if __name__ == '__main__':
    app.run(debug=True)  # port=3033)
