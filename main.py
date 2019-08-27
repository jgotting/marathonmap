#!/usr/bin/env python
# coding: utf-8

# # Marathonkandidater 2010
# Syftet med denna notebook är att på en karta (Open Street Map) plotta ut tänkbara kandidater för Marathons hösten 2020.

#Importera våra moduler
# import os
from flask import Flask
#import requests
import pandas as pd
import folium
from folium.plugins import MarkerCluster
#from geopy.geocoders import Nominatim

#Läs in datafil
df = pd.read_csv('marathon2020.csv', sep=';', encoding='latin1')
#
# Fixa visualisering
m = folium.Map(
    location=[40.613293, 12.657610],
    zoom_start=5
,
    tiles='Stamen Terrain'
)

# Placera markers på kartan
for index, row in df.iterrows(): 
    tooltip = '<a href="'+ row["URL"] + '" target="_blank">' + row["Location"] + '</a>'
    folium.Marker([row['Latitude'], row['Longitude']], popup=tooltip + '<b>' + row["Date"] + '</b>' , tooltip=row["Namn"]).add_to(m)

app = Flask(__name__)

@app.route('/')
def index():
    
# Display map    
    return m._repr_html_()
if __name__ == '__main__':
    app.run(debug=True)


