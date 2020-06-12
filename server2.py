from fastapi import FastAPI    
import os
from logger import trigger_log_save
from MovieAPI import get_movie_info

app = FastAPI()

@app.get("/")
def hello_world():
    trigger_log_save()
    return {"hello":"world"}

@app.get("/abc")
def abc():
    trigger_log_save()
    return ("Hello World")

movie = ""
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'Movie Files', f'{movie}.txt')

@app.get(f"/{movie}")
def display_movie_info():
    get_movie_info(movie)
    trigger_log_save()
    with open(file_path, 'r') as f:
        info = f.read()

    return info