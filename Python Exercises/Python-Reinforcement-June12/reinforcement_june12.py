import json
import requests

ottawa_wards_response = requests.get(
    'https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
data = ottawa_wards_response.json()

for result in data['objects']:
    print(result['name'])

house_of_rep = requests.get('https://represent.opennorth.ca/representatives/house-of-commons/')
representatives = house_of_rep.json()

for rep in representatives['objects']:
    print(f"Party: {rep['party_name']}")
    print(f"Name: {rep['first_name']} {rep['last_name']}")
    print("--------------------------------------------")

