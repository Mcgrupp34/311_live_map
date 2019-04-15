import pandas as pd
import os

from mapboxgl.viz import *
from mapboxgl.utils import *

#mapbox token
token = os.getenv('pk.eyJ1IjoiemFja3dhbGtlciIsImEiOiJjanNxZnc1dzUwazYxNDRveDNvc2ZnM2RpIn0.ZJMacn_-hQpW8DEaQAyxuw')

# Load data from sample csv
data_url = 'https://raw.githubusercontent.com/mapbox/mapboxgl-jupyter/master/examples/data/cdec.csv'
df = pd.read_csv(data_url)

# Convert Elevation series to float
df['Elevation (feet)'] = df['Elevation (feet)'].astype(float)

# Clean up by dropping null rows
df = df.dropna(axis=1, how='all')

df.head(2)

# Create geojson data object
def make_geojson(data_csv):
    df_to_geojson(df.fillna(''),
        filename='points.geojson',
        properties=['CDEC ID', 'CNRFC ID', 'Gage Type', 'Elevation (feet)'],
        precision=4)

# Assign color stops
category_color_stops = [['reservoir', 'rgb(211,47,47)'],
                            ['river', 'rgb(81,45,168)'],
                             ['snow', 'rgb(2,136,209)'],
                          ['precip', 'rgb(139,195,74)'],
                             ['temp', 'rgb(255,160,0)']]

# Initialize CircleViz with Categorical Measure Data
viz = CircleViz('points.geojson',
    access_token=token,
    height='500px',
    label_property='CDEC ID',
    color_property='Gage Type',
    color_default='grey',
    color_function_type='match',
    color_stops=category_color_stops,
    radius=2,
    center=(-121, 38.5),
    zoom=4.5)

# Render map
html = open("test_map2.html", "w")
html.write(viz.create_html())
html.close()
