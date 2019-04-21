import pandas as pd, requests, json
from sodapy import Socrata

#api call
client = Socrata("data.cityofnewyork.us", "APPLICATION_KEY")

results = client.get("fhrw-4uyv", limit=5000)

#convert pandas dataframe
results_df = pd.DataFrame.from_records(results)

#safety clean up by dropping null rows
results_df = results_df.dropna(axis=1, how='all')

#convert lat-long to floats and change address to sentence case
results_df['latitude'] = results_df['latitude'].astype(float)
results_df['longitude'] = results_df['longitude'].astype(float)
results_df['incident_address'] = results_df['incident_address'].str.title()

#drop unnecessary columns
useful_cols = ['complaint_type', 'descriptor', 'incident_address', 'latitude', 'longitude']
results_useful_df = results_df[useful_cols]

def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    """
    Turn a dataframe containing point data into a geojson formatted python dictionary

    df : the dataframe to convert to geojson
    properties : a list of columns in the dataframe to turn into geojson feature properties
    lat : the name of the column in the dataframe that contains latitude data
    lon : the name of the column in the dataframe that contains longitude data
    """

    # create a new python dict to contain our geojson data
    geojson = {'type':'FeatureCollection', 'features':[]}

    # loop through each row in the dataframe and convert each row to geojson format
    for _, row in df.iterrows():
        # create a feature template to fill in
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}

        # fill in the coordinates
        feature['geometry']['coordinates'] = [row[lon],row[lat]]

        # for each column, get the value and add it as a new feature property
        for prop in properties:
            feature['properties'][prop] = row[prop]

        # add this feature (aka, converted dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)

    return geojson


geojson_dict = df_to_geojson(results_useful_df, properties=useful_cols)
geojson_str = json.dumps(geojson_dict, indent=2)

#save the geojson result to a file
output_filename = '311_data.js'
with open(output_filename, 'w') as output_file:
    output_file.write('var dataset = {};'.format(geojson_str))
