import json, requests
import pandas as pd

def atcoder_json(user_name):
	BASE_URL = "https://beta.atcoder.jp/users/{}/history/json"
	json_data = requests.get(BASE_URL.format(user_name))
	json_data = json.loads(json_data.content.decode())
	return json_data

def atcoder_data_frame(user_name):
	return pd.DataFrame(atcoder_json(user_name))