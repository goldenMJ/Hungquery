# import the Flask class from the flask module
from flask import Flask, render_template, jsonify
from flask import request
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import os
import csv

# ################################################
# # Database Setup
# ################################################
# engine = create_engine("sqlite:///hungquery.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# Passenger = Base.classes.recipes

# # # Create our session (link) from Python to the DB




#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)


