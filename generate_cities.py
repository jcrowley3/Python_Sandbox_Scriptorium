import requests
import json



# Define the API endpoint for cities
# endpoint = "https://api.geodb.com/v1/cities"
endpoint = 'https://wft-geo-db.p.rapidapi.com/v1'
response = requests.get(endpoint)

# Define your API key
api_key = "your_api_key_here"

# add API key to api_key



# Make a GET request to the API
params = {
    "limit": 1000,
    "offset": 0,
    "radius": 20000,
    "sort": "population"
}
headers = {
    "Authorization": "Bearer " + api_key
}
response = requests.get(endpoint, params=params, headers=headers)

# Parse the response as a JSON object
data = json.loads(response.text)

# Extract the list of cities
cities = [city["name"] for city in data["data"]]

# Write the list of cities to a .txt file
with open("cities.txt", "w") as f:
    for city in cities:
        f.write(city + "\n")



