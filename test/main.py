# https://covidtracking.com/data/api
import json
import requests

import pandas as pd

url = 'https://api.covidtracking.com/v1/us/daily.json'

resp = requests.request("GET", url)
data_as_json = resp.text.encode('utf8')

print(json.loads(data_as_json))

print(pd.read_json(data_as_json))