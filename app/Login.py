import requests
import json
from app.AppConfig import APPKEY, HOST, APPVERSION, BRAND, DEVICETOKEN, DEVICETYPE, MOBILETYPE, SYSVERSION, CONTENTTYPE, USERAGENT
from app.SaveUserData import save_data
from utils.Md5Util import *
from utils.SignUtil import *

def login(phone, password):
    password = string_to_md5(password)
    body = {
        "appVersion": APPVERSION,
        "brand": BRAND,
        "deviceToken": DEVICETOKEN,
        "deviceType": DEVICETYPE,
        "mobileType": MOBILETYPE,
        "password": password,
        "sysVersion": SYSVERSION,
        "userPhone": phone
    }

    body = json.dumps(body)
    headers = {
        "appKey": APPKEY,
        "sign": get_sign(None, body),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }

    response = requests.post(HOST + 'v1/auth/login/password', headers=headers, data=body)
    data = response.json()
    msg = data["msg"]

    if data["code"] == 10000:
        save_data(data["response"])
        return True

    else:
        return False

def check_login_status(token):
    logged = False

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
        logged = True
        return logged
    else:
        return logged
