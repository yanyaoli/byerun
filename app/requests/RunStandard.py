import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign
from app.Login import check_login_status


def query_run_standard(token):
    global sign
    if check_login_status() == False:
        return None, None, None, None, None
    else:
        data = load_data()
        schoolId = data.get('schoolId')
        token = data.get('token')
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
        print(headers)
        response = requests.get(HOST + "v1/unirun/query/runStandard", headers=headers, params=query)
        data = response.json()
        msg = data["msg"]
        try:
            if data["code"] == 10000:
                standardId = data["response"]["standardId"]
                schoolId = data["response"]["schoolId"]
                boyOnceTimeMin = data["response"]["boyOnceTimeMin"]
                boyOnceTimeMax = data["response"]["boyOnceTimeMax"]
                semesterYear = data["response"]["semesterYear"]
                return standardId, schoolId, boyOnceTimeMin, boyOnceTimeMax, semesterYear
            else:
                return msg
        except RuntimeError as e:
            print(f"发生错误：{e}")