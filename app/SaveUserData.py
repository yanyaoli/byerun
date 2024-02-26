import json
import os

def save_data(data):
    data_to_save = data.copy()
    data_to_save["token"] = data["oauthToken"]["token"]
    data_to_save["refreshToken"] = data["oauthToken"]["refreshToken"]
    del data_to_save["oauthToken"]
    with open('user_data.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f)

def load_data():
    try:
        if os.path.getsize('user_data.json') > 0:
            with open('user_data.json', 'r') as f:
                return json.load(f)
        else:
            return None
    except FileNotFoundError:
        return None

