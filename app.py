# import the Flask class from the flask module
from flask import Flask, render_template
from flask import request
import pandas as pd 
import os
import csv

# create the application object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')  
if __name__ == "__main__":
    app.run(debug=True)