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
# Database Setup
################################################
# Connect to the database 
# rds_connection_string = "<insert user name>:<insert password>@localhost:5432/customer_db"
rds_connection_string = "postgres:5432@localhost:5432/hunquery"
engine = create_engine(f'postgresql://{rds_connection_string}')
print(engine.table_names())
# # Create our session (link) from Python to the DB




#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def Index():
    return render_template('index.html') 

@app.route("/addnew", methods=['GET', 'POST'])
def Addnew():
    if request.method == 'GET':
        return render_template('addnew.html')
    else:
        data = request.form
        print(data)
        return jsonify(data)



# to start server
if __name__ == "__main__":
    app.run(debug=True)


