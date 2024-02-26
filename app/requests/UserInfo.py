import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign


def get_user_info():
    data = load_data()
    token = data["token"]

    headers = {
        "token": token,
        "appKey": APPKEY,
        "sign": get_sign(None,None),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }
    response = requests.get(HOST + "v1/auth/query/token", headers=headers)
    data = response.json()
    if data["code"] == 10000:
        return data
    else:
        msg = data["msg"]
        return msg