# Uses the Open Notify open source API from NASA. 
# check it out: http://open-notify.org/

import requests
from datetime import datetime

print("\nThis program uses NASA data and the open source Open Notify API. Check it out at http://open-notify.org")

print("\nAbout the International Space Station (ISS)")
print("===========================================")
print("The ISS travels at approximately 17,150 miles per hour (27,600 kilometers per hour), and completes an orbit every 92 minutes.")


# ISS Pass Times
##############################################
# params for iss-pass : latitude and longitude
# To find a latitude and longitude to use, try https://www.latlong.net/
parameters = {"lat": 45.5214400  , "lon": -122.6769200}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

# jsonify the response.
iss_data = response.json()

print(f"\nISS Pass Data for your location ({parameters['lat']} longitude: {parameters['lon']})")
print("===============================")
for datapoint in iss_data['response']:
    print(f"Risetime: {datetime.utcfromtimestamp(datapoint['risetime']).strftime('%H:%M:%S')}  Duration: {datapoint['duration']} seconds")

# ISS Current Location
###############################################

response = requests.get("http://api.open-notify.org/iss-now.json")

# jsonify the response.
iss_loc = response.json()

ts = int(iss_loc['timestamp'])

print("\nThe ISS is currently at:")
print("========================")
print(f"Position: \nLATITUDE: {iss_loc['iss_position']['latitude']}  LONGITUDE: {iss_loc['iss_position']['longitude']}" )
print(f"\nDate/Time: \n{datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}")


# People in Space
###############################################

# Show the current number of people in space! 
response = requests.get("http://api.open-notify.org/astros.json")

astros = response.json()

print("\nHow many astronauts are in space right now?")
print("===========================================")
print(f"There are currently {astros['number']} astronauts in space.")
