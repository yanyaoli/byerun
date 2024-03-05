import requests
from app.AppConfig import HOST, APPKEY, CONTENTTYPE, USERAGENT
from utils.SignUtil import get_sign
from app.Login import check_login_status


def query_run_standard(token, schoolId):
    if check_login_status(token) == False:
        return None, None, None, None, None
    else:
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