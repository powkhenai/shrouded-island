from flask import Flask, render_template, session, redirect, url_for, request
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    if 'username' in session:
       return "Logged in as: %s" % session['username']
    return "Not logged in."

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/<name>')
def index(name=None):
    return render_template('test.html', username=name)

@app.route('/dbtest')
def dbtest():
    conn = psycopg2.connect(host='ec2-75-101-142-182.compute-1.amazonaws.com', port=5432, database='da3bngkdmd0kr1', user='guvtlvmrcrycgj', password='2fd7a74f97b55291f350f601979e4826be99a2f6e68f3c579d3644426fb6329d')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM widgets;")
    results = cursor.fetchall()
    print results
    return "hello"
