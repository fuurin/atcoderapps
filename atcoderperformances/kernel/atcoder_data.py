import json, requests
import pandas as pd

def AtCoderJSON(user_name):
	BASE_URL = "https://beta.atcoder.jp/users/{}/history/json"
	json_data = requests.get(BASE_URL.format(user_name))
	json_data = json.loads(json_data.content.decode())
	return json_data

def AtCoderDataFrame(user_name):
	return pd.DataFrame(AtCoderJSON(user_name))