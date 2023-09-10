import matplotlib as plt
import folium
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import time
# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.read_csv("C:/Users/kannan/Desktop/unnati_phase1_data_revised.csv")
#only show find the alert in each location count value greater than 1
fil=data.groupby(['Lat','Long']).size().sort_values(ascending=False)[data.groupby(['Lat','Long']).size().sort_values(ascending=False)>4]
c=fil[fil>7].reset_index()
c=c.head(6)
#initialize geolocater
geolocator = Nominatim(user_agent="myGeocoder")
latitude=12.992198
longitude=80.182455
# Create a folium map centered around the first location in the DataFrame
map = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker([latitude,longitude],).add_to(map)
#folium marker colour as red
folium.CircleMarker([latitude,longitude],radius=5,color='red',fill=True,fill_color='red',fill_opacity=0.5).add_to(map)

custom_icon = folium.Icon(color='green')

# Add markers for hospitals and schools near the location
for index,row in c.iterrows():
    latitude=row['Lat']
    longitude=row['Long']
    folium.Marker([latitude,longitude],).add_to(map)
#folium marker colour as red
    folium.CircleMarker([latitude,longitude],radius=5,color='red',fill=True,fill_color='red',fill_opacity=0.5).add_to(map)
    Location=geolocator.reverse((latitude,longitude))
    for place in ["Hospital", "school","Airport","Railway Station","Bus Stand","collage",]:
        query = '{} near {}'.format(place, Location)

        # Create the geocode for the query

        try:
                results = geolocator.geocode(query)

                if results:
                    lat = results.latitude
                    lng = results.longitude
                    label = place
                    folium.Marker([lat, lng], popup=label,icon=folium.Icon(color='green')).add_to(map)

        except Exception as e:
            print("Error geocoding:", e)
map
