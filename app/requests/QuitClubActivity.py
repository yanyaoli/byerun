import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign

def queryMySemesterClubActivity(token):
    data = load_data()
    token = data.get('token')

    headers = {
        "token": token,
        "appKey": APPKEY,
        "sign": get_sign(None,None),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }
    response = requests.get(HOST + "v1/clubactivity/queryMySemesterClubActivity", headers=headers)
    data = response.json()
    if data["code"] == 10000:
        print(data)
        if len(data["response"]) >= 2:
            configurationId = data["response"][0]["configurationId"]
            return configurationId
        else:
            configurationId = data["response"][0]["configurationId"]
            return configurationId
    else:
        return data["msg"]


def quit_club_activity(token):
    data = load_data()
    token = data.get('token')

    configurationId = queryMySemesterClubActivity(token)
    query = {
        "configurationId": configurationId,
        "type": "2"
    }
    headers = {
        "token": token,
        "appKey": APPKEY,
        "sign": get_sign(query,None),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }
    print(headers)
    response = requests.get(HOST + "v1/clubactivity/joinOrCancelSchoolSemesterActivity", headers=headers, params=query)
    data = response.json()
    msg = data["msg"]
    if data["code"] == 10000:
        message = data["response"]["message"]
        return message
    else:
        return msg
