import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign


def count_valid_sign_up(token):
    data = load_data()
    token = data.get('token')
    studentId = data.get('studentId')
    query = {
        "studentId": studentId
    }
    headers = {
        "token": token,
        "appKey": APPKEY,
        "sign": get_sign(query,None),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }
    response = requests.get(HOST + "v1/clubactivity/countValidSignUp", headers=headers, params=query)
    data = response.json()
    if data["code"] == 10000:
        joinNum = data["response"]["joinNum"]
        validNum = data["response"]["validNum"]
        result = f'累计参加俱乐部活动：{joinNum}次，有效签到次数：{validNum}次'
        return result
    else:
        raise RuntimeError(data["msg"])