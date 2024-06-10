from flask import Flask, render_template, request, redirect, url_for, flash, render_template_string
from flask_wtf import FlaskForm
import folium
from folium import plugins
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
    

# create a layer for bubble map using FeatureGroup
    dataDf = pd.read_excel('rmap.xlsx')
    #print(dataDf)

    mapObj = folium.Map(location=[22.724381, 75.884383 ],
                        zoom_start=13)
    bordersStyle = {"color": 'green', 'weight': 2, 'fillOpacity': 0}
    bordersLayer = folium.GeoJson(
    data="states_india.geojson",
    name="Borders",
    style_function=lambda x: bordersStyle)
    bordersLayer.add_to(mapObj)
    # add a marker to the map object
    for i in range(len(dataDf)):
        folium.Marker([dataDf.iloc[i][2], dataDf.iloc[i][3]],
                    popup="<i><B>"+str(dataDf.iloc[i][1])+" <B> </i>").add_to(mapObj)
    
    # set iframe width and height
    mapObj.get_root().width = "1900px"
    mapObj.get_root().height = "1900px"

    # derive the iframe content to be rendered in the HTML body
    iframe = mapObj.get_root()._repr_html_()

    # return a web page with folium map components embeded in it. You can also use render_template.
    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    
                    {{ iframe|safe }}
                    
                </body>
            </html>
        """,
        iframe=iframe,
    )
@app.route("/hmap.html")
def hmap():
    dataDf = pd.read_excel('hmap.xlsx')
    #print(dataDf)

    mapObj = folium.Map(location=[22.7269748, 75.87981065 ], zoom_start=13)
    # Add custom tiles with attribution
    
    bordersStyle = {"color": 'green', 'weight': 2, 'fillOpacity': 0}
    folium.GeoJson(
    data=(open("states_india.geojson", 'r').read()),
    name="India",
    style_function=lambda x: bordersStyle).add_to(mapObj)

    
# add layer control over the map
    folium.LayerControl().add_to(mapObj)
    # add a marker to the map object
    for i in range(len(dataDf)):
        folium.Marker([dataDf.iloc[i][2], dataDf.iloc[i][3]],
                    popup="<i><B>"+str(dataDf.iloc[i][1])+" <B> </i>").add_to(mapObj)
    
    # set iframe width and height
    mapObj.get_root().width = "1900px"
    mapObj.get_root().height = "1900px"

    # derive the iframe content to be rendered in the HTML body
    iframe = mapObj.get_root()._repr_html_()

    # return a web page with folium map components embeded in it. You can also use render_template.
    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    
                    {{ iframe|safe }}
                    
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
