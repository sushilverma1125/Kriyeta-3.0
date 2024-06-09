from flask import Flask, render_template, request, redirect, url_for, flash, render_template_string
from flask_wtf import FlaskForm
import folium
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from sklearn.neighbors import KNeighborsClassifier
import cv2
import pandas as pd
from win32com.client import Dispatch
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
import os
import time
import pyttsx3
from flask import Flask, render_template, request, jsonify

from dotenv import load_dotenv
import os
import pathlib
import textwrap


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")
@app.route("/index.html")
def home():
   return render_template("index.html")

@app.route("/explore.html")
def explore():
   return render_template("explore.html")

@app.route("/rmap.html")
def rmap():
    mapObj = folium.Map(location=[17.4127332, 78.078362],
                        zoom_start=10)
    # add a marker to the map object
    folium.Marker([17.4127332, 78.078362],
                  popup="<i>This a marker</i>").add_to(mapObj)
    folium.Marker([17.4117332, 78.178362],
    
                  popup="<i>This a marker</i>").add_to(mapObj)
    folium.Marker([27.4117332, 78.178362],
                  popup="<i>This a marker</i>").add_to(mapObj)

    # set iframe width and height
    mapObj.get_root().width = "700px"
    mapObj.get_root().height = "500px"

    # derive the iframe content to be rendered in the HTML body
    iframe = mapObj.get_root()._repr_html_()

    # return a web page with folium map components embeded in it. You can also use render_template.
    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using iframe to render folium map in HTML page</h1>
                    {{ iframe|safe }}
                    <h3>This map is place in an iframe of the page!</h3>
                </body>
            </html>
        """,
        iframe=iframe,
    )
    
@app.route("/form.html", methods=['GET', 'POST'])
def form():
    
    if request.method=='POST':
        
        des=request.form.get('description')
        print(des)
        return render_template("form.html")
    return render_template("form.html")
if __name__ == "__main__":  
    app.run(debug=True, port=5002)
