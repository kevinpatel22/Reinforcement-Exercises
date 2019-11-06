import json
import requests

res = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
body = json.loads(res.content)

for country in body:
    if country['name'] == 'United States of America':
        print(body.index(country))

url = body[220]['legislatures'][0]['popolo_url']
house_of_rep = requests.get(url)
representatives = json.loads(house_of_rep.content)
politician = representatives['persons'][5]['name']


print(politician)





