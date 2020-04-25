# Uses the Open Notify open source API from NASA. 
# check it out: http://open-notify.org/

import requests
from datetime import datetime
from colorama import init, Fore, Back, Style
init()

print(f"\nThis program uses NASA data and the open source Open Notify API. Check it out at {Fore.GREEN}http://open-notify.org{Style.RESET_ALL}")

print(f"\n{Fore.CYAN}About the International Space Station (ISS){Style.RESET_ALL}")
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

print(f"\n{Fore.CYAN}ISS Pass Data for your location{Style.RESET_ALL} ({Fore.GREEN}latitude:{Style.RESET_ALL} {Fore.YELLOW}{parameters['lat']} {Style.RESET_ALL}{Fore.GREEN}longitude:{Style.RESET_ALL} {Fore.YELLOW}{parameters['lon']}{Style.RESET_ALL})")
print("===============================")
for datapoint in iss_data['response']:
    print(f"{Fore.GREEN}Risetime:{Style.RESET_ALL} {Fore.YELLOW}{datetime.utcfromtimestamp(datapoint['risetime']).strftime('%H:%M:%S')}{Style.RESET_ALL}  {Fore.GREEN}Duration:{Style.RESET_ALL} {Fore.YELLOW}{datapoint['duration']} seconds{Style.RESET_ALL}")

# ISS Current Location
###############################################

response = requests.get("http://api.open-notify.org/iss-now.json")

# jsonify the response.
iss_loc = response.json()

ts = int(iss_loc['timestamp'])

print(f"\n{Fore.CYAN}The ISS is currently at:{Style.RESET_ALL}")
print("========================")
print(f"{Fore.GREEN}Position:{Style.RESET_ALL} \nLATITUDE: {Fore.YELLOW}{iss_loc['iss_position']['latitude']}{Style.RESET_ALL}  LONGITUDE: {Fore.YELLOW}{iss_loc['iss_position']['longitude']}{Style.RESET_ALL}" )
print(f"\n{Fore.GREEN}Date/Time:{Style.RESET_ALL} \n{datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")


# People in Space
###############################################

# Show the current number of people in space! 
response = requests.get("http://api.open-notify.org/astros.json")

astros = response.json()

print(f"\n{Fore.CYAN}How many astronauts are in space right now?{Style.RESET_ALL}")
print("===========================================")
print(f"There are currently {Fore.YELLOW}{astros['number']} {Style.RESET_ALL}astronauts in space.\n")
