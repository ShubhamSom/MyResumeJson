import json
import pprint

import urllib3


def fetch_json(url, *args, **kwargs):
    http = urllib3.PoolManager(num_pools=3)
    response = http.request("GET", url)
    data_str = response.data.decode("UTF-8")
    print(f'data_str:type:{type(data_str)}')
    data = json.loads(data_str)  # load into json obj
    print(f'data:type:{type(data)}')
    pprint.pprint(data)

token = ""
url = f"https://raw.githubusercontent.com/ShubhamSom/MyResumeJson/main/resume.json"
print(url)
fetch_json(url)
