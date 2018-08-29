# Uses the Open Notify open source API from NASA. 
# check it out: http://open-notify.org/

import requests
from datetime import datetime

print("\nThis program uses data from NASA's open source Open Notify API. Check it out at http://open-notify.org")

print("\nAbout the International Space Station (ISS)")
print("===========================================")
print("The ISS travels at approximately 17,150 MPH and completes an orbit every 92 minutes.")


# ISS Pass Times
##############################################
# params for iss-pass : latitude and longitude
parameters = {"lat": 45.5214400  , "lon": -122.6769200}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

# jsonify the response.
iss_data = response.json()

print("\nISS Pass Data for your location (latitude: {} longitude: {})".format(parameters['lat'], parameters['lon']))
print("===============================")
for datapoint in iss_data['response']:
    print("Risetime: {}  Duration: {} sec ".format( (datetime.utcfromtimestamp(datapoint['risetime']).strftime('%H:%M:%S')),datapoint['duration']  ))

# ISS Current Location
###############################################

response = requests.get("http://api.open-notify.org/iss-now.json")

# jsonify the response.
iss_loc = response.json()

ts = int(iss_loc['timestamp'])

print("\nThe ISS is currently at:")
print("========================")
print("Position: \nLATITUDE: {}  LONGITUDE: {}".format(iss_loc["iss_position"]['latitude'], iss_loc["iss_position"]['longitude']) )
print("\nDate/Time: \n{}".format(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')))


# People in Space
###############################################

# Show the current number of people in space! 
response = requests.get("http://api.open-notify.org/astros.json")

astros = response.json()

print("\nHow many astronauts are in space right now?")
print("===========================================")
print("There are currently {} astronauts in space.\n".format(astros["number"]))
