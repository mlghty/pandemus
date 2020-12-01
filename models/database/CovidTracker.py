import requests
import json
import pandas

class CovidTracker:
    def __init__(self):
        pass

    def fetch_json(self, url):
        resp = requests.request("GET", url)
        json_data = resp.text.encode('utf8')
        return json_data
    
    def get_national_data(self):

        json_national_cases = self.fetch_json('https://api.covidtracking.com/v1/us/daily.json')
        national_cases = pandas.read_json(json_national_cases)
        
        # # idk how to python
        # cases_per_day = []
        # for current_day in daily_national_cases:
        #     case = {}
        #     case['positive'] = current_day['positive']
        #     case['date'] = current_day['date']
        #     cases_per_day.append(case)

        return national_cases.loc[:, ['date', 'positive']]