
  This project attempts to create a 'live' map of 311 data for the City of New York. The data is not truly live since the API is updated only once a day.

  The project has two parts: a Python script that makes an API call and performs data manipulations before converting to a
geojson file, and an HTML/Javascript file that handles the rendering of the webmap.
The python file calls a Socrata API for the City of New York, converts that data into a Pandas Dataframe, drops unwanted
columns, and then converts to geojson before writing to a new file. The HTML and Javascript calls the Mapbox GL API and
renders a basemap that was designed in Mapbox Studio. The geojson file from the Python script is added to the map as a layer
and styled by data properties. Additionally, a legend, a popup on feature-click, and various map details are controlled
through the JS. The user is able to pan and zoom the map, and click on individual features for more details.
