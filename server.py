# flask 
# is a framework for building servers
# contains all the component parts 
# flask and django are the main frameworks
# Flask is smaller but django has heaps of tools

# create a virtual env folder in your web server folder 
# cd one level above web sevrer folder
# python3 -m venv web\ server/
# creates a venv in the web server folder
# Activate the venv:
# source web\ server/bin/activate 
# the exact command depends on the type of shell being used
# https://docs.python.org/3/library/venv.html
# the above is the command for zsh

# now we can install packages in the venv
# Quick start guide
# https://flask.palletsprojects.com/en/2.2.x/quickstart/

# In terminal:
# export FLASK_APP=<filename>
# flask run
# it will automatically deploy at
# http://127.0.0.1:5000/
# which is the localhost
# make changes and re execute flask run
# don't want to have to restart the server
# every time we make a change. YOu will see
# that debug mode is off
# turn it on by executing
# export FLASK_ENV=development
# or export FLASK_DEBUG=1
# then it will say debugger is active
# the server will auto restart when you make changes

# when pushing to git don't need the virtual env
# go pip freeze > requirements.txt
# instead of pushing your whole virtual env.

# flask converts text to html so the browser can understand it
# or you can use render_template to use your own html files

# static files are those which don;t change such as css and js files
# they live in a folder called static

# adding a favicon:
# https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
# <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
# flask is a templating language where we can build stuff dynamically
# e.g., if we do {{ 4 + 5}} in our html file, flask
#  sees it as a python expression that needs to be evaluated as python
# it is good to build url instead of hardcoding (see flask docs)

# variable rules:
# enables us to create dynamic routes
# @app.route("/<username>")
# flask sees username as a variable it can pass into the 
# see the hello world function and index.html
# there are different rules, e.g., force integer, float 
# etc. See documentation under variable rules. Will get Not Found
# if breaking the rules

# MIME types
# multi purpose internet mail extensions
# browsers use the mime type to determine how to process a url
# not the file extension

# there are heaps of html templates you can use for free
# https://html5up.net/
# https://themewagon.com/author/mashuptemplate/
# https://www.creative-tim.com/bootstrap-themes/free

# deploying app online:
# use pythonanywhere,https://www.pythonanywhere.com/
# clone the repo https.
# open a bash console and go git clone <link>
# note: this is a linux terminal 
# All your files will appear in files on the dashboard
# we get one free web app with free membership
#  https://help.pythonanywhere.com/pages/Flask
# enter the path to the source code.
# follow the instructions at the link for setting up the venv and install flask
# or run pip install -r requirements.txt if many things to install
# specify path to venv in the webapp page
# update the config file so the path to your app is correct
# and its importing from the code page.
# database.csv will update in pythonanywhere

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
# print(__name__)

# decorator - gives extra server tools
# define a function every time we hit slash
# It is repetitive to copy and paste code for each page
# of your website.
# we can make it less repetitive using the second function below

@app.route("/")
def my_home():
    # render_template automatically looks 
    # in a folder called templates 
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)

def write_to_csv(data):
    # saving the form entries to a database in csv
    # databases exist to store data that persists. 
    # the server communicates with a db to store information
    # eg mongoDB/postgreSQL
    # postgres is relational.
    # mongoDB Is non relational (noSQL)
    # it depends on your need
    entries = data.values()
    with open('database.csv', 'a') as db_file:
        writer = csv.writer(db_file)
        writer.writerow(entries)

# accessing request data
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # we will go to this end point from contact.html when
    # the user clicks send. 
    # see <form action="submit_form"
    # all the attributes need a name so we can grab the data
    if request.method == 'POST':
        try:
            # get all form data as dict
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database :('
    else:
        return 'something went wrong try again.'

# @app.route("/index.html")
# def home():
#     return render_template('index.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
