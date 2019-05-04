### Project Description
  This project attempts to create a 'live' map of 311 data for the City of New York. The data is not truly live since the API is updated only once a day.

  The project has two parts: a Python script that makes an API call and performs data manipulations before converting to a
geojson file, and an HTML/Javascript file that handles the rendering of the webmap. The python file calls a Socrata API for
the City of New York, converts that data into a Pandas Dataframe, drops unwanted columns, and then converts to geojson before
writing to a new file. The HTML and Javascript calls the Mapbox GL API and renders a basemap that was designed in Mapbox
Studio. The geojson file from the Python script is added to the map as a layer and styled by data properties. Geojson is used for it's ease in implementing into a webmap, but becareful of errors cropping up in your file from  Additionally, a
legend, a popup on feature-click, and various map details are controlled through the JS. The user is able to pan and zoom the
map, and click on individual features for more details.

### Instructions
  To recreate this project you will need an Application Key from opendata.cityofnewyork.us and a Public Key from Mapbox.com. Use your Application Key in the Python file where it says "APP KEY" and your Public Key in the HTML file where it says 'MAPBOX PUBLIC KEY'. Change the 'useful_cols' in the python file to any other columns you find interesting to subsect the data to your desires. 
