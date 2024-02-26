import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign

def query_school_bound(token):
    data = load_data()
    token = data.get('token')
    schoolId = data.get('studentId')
    query = {
        "schoolId": schoolId
    }

    headers = {
        "token": token,
        "appKey": APPKEY,
        "sign": get_sign(query,None),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }
    response = requests.get(HOST + "v1/unirun/querySchoolBound", headers=headers, params=query)
    data = response.json()
    if data["code"] == 10000:
        return data
    else:
        raise RuntimeError(data["msg"])