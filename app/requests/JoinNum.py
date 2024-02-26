import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign

def get_join_num(token):
    data = load_data()
    token = data.get('token')
    schoolId = data.get('schoolId')
    studentId = data.get('studentId')
    query = {
        "schoolId": schoolId,
        "studentId": studentId
    }
    headers = {
        "token": token,
        "appKey": APPKEY,
        "sign": get_sign(query,None),
        "Content-Type": CONTENTTYPE,
        "User-Agent": USERAGENT
    }
    response = requests.get(HOST + "v1/clubactivity/getJoinNum", headers=headers, params=query)
    data = response.json()
    if data["code"] == 10000:
        totalNum = data["response"]["totalNum"]
        joinNum = data["response"]["joinNum"]
        runTotalNum = data["response"]["runTotalNum"]
        runJoinNum = data["response"]["runJoinNum"]
        result = f'俱乐部完成率：{joinNum}/{totalNum}次\n校园跑完成率：{runJoinNum}/{runTotalNum}次'
        return result
    else:
        msg = data["msg"]
        return msg