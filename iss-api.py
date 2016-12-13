# Use the Open Notify open source API from NASA. 
# check it out: http://open-notify.org/

import requests

# params for iss-pass : latitude and longitude
parameters = {"lat": 45.5214400  , "lon": -122.6769200}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

# jsonify the response.
iss_data = response.json()

print("ISS Pass Data for your location")
print("===============================")
for datapoint in iss_data['response']:
	print(datapoint)

# Show the current number of people in space! 
response = requests.get("http://api.open-notify.org/astros.json")

astros = response.json()

print("\nThere are currently {} astronauts in space.".format(astros["number"]))