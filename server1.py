from flask import Flask
from logger import trigger_log_save
import requests
import os
from MovieAPI import get_movie_info

app = Flask(__name__)

movie = ''

@app.route('/', methods = ['GET', 'POST'])    #Function to the endpoint of url
def homepage():
    global movie
    return f"This is Flask. Add '/movie' to the url to see information about {movie}."    

@app.route('/abc', methods = ['GET'])
def abc():
    return "abc"