#!/usr/bin/env python
# coding: utf-8

# # Marathonkandidater 2010
# Syftet med denna notebook är att på en karta (Open Street Map) plotta ut tänkbara kandidater för Marathons hösten 2020.



#Importera våra moduler
# import os
from flask import Flask
import pandas as pd
import requests
import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim

#os.listdir()
#Läs in datafil
df = pd.read_csv('Maraton 2019.csv', sep=';')
df.head()


# dropping null value columns to avoid errors 
df.dropna(inplace = True) 
  
# new data frame with split value columns 
new = df["Plats"].str.split("|", n = 1, expand = True) 
  
# making separate first name column from new data frame 
df["Location"]= new[0] 
  
# making separate last name column from new data frame 
df["Date"]= new[1] 
  
# Dropping old Name columns 
df.drop(columns =["Plats"], inplace = True) 
  
# df display 
df.head()

# Fixa visualisering

# Translate location to coordinates
nom = Nominatim(user_agent="my-application")
place = "Palma de Mallorca, Spain"
n=nom.geocode(place)
# print(place)
# print(n.latitude, n.longitude)

#starting map
m = folium.Map(
#location=[n.latitude, n.longitude],
location=[n.latitude, n.longitude],
zoom_start=5
,
tiles='Stamen Terrain'
)

#folium.Marker(n.latitude, n.longitude)

# Geopy för att mappa Location mot coordinater
for index, row in df.iterrows(): 
    n=nom.geocode(row["Location"])
    tooltip = '<a href="'+ row["URL"] + '" target="_blank">' + row["Location"] + '</a>'
    folium.Marker([n.latitude, n.longitude], popup=tooltip + '<b>' + row["Date"] + '</b>' , tooltip=row["Namn"]).add_to(m)
# folium.Marker([n.latitude, n.longitude]).add_to(m)


app = Flask(__name__)


@app.route('/')
def index():
    
# Display map    
    return m._repr_html_()
if __name__ == '__main__':
    app.run(debug=True)


