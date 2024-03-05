import json
import requests
import datetime
from app.AppConfig import HOST, APPKEY, APPVERSION, BRAND, MOBILETYPE, SYSVERSION, CONTENTTYPE, USERAGENT
from app.SaveUserData import load_data
from utils.SignUtil import get_sign
from utils.TrackUtil import genTrackPoints
from app.requests.RunStandard import query_run_standard

NOTICE = [
    "我认为这种事情是不可能的",
    "太快了",
    "要死了",
    "你正在自毁",
    "你正在自残",
    "你的锻炼正造成身体上的损伤",
    "六分是养身",
    "七分是自娱",
    "八分是治愈"
]

def getDate():
    return (datetime.datetime.now() - datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")

def check_speed(runDistance, runTime):
    average = 1.0 * runTime / runDistance * 1000
    if average < 6:
        print("八分是治愈，七分是自娱，六分是养身，五分是自伤，四分是自残，三分是自毁。")
        print(f"你的配速是：{average:.2f} 分钟/公里, {NOTICE[int(average)]}")
    else:
        print(f"平均配速：{average:.2f} 分钟/公里")
    return average

def new_run_record(runDistance, runTime, map_choice, token, userId, studentName, schoolId):
    average = check_speed(runDistance, runTime)
    if average < 6:
        notice = "速度过快，已停止执行后续请求"
        return notice
    else:
        semesterYear = query_run_standard(token, schoolId)[-1]

        body = {
            "againRunStatus": "0",
            "againRunTime": 0,
            "appVersions": APPVERSION,
            "brand": BRAND,
            "mobileType": MOBILETYPE,
            "sysVersions": SYSVERSION,
            "trackPoints": genTrackPoints(runDistance, map_choice),
            "distanceTimeStatus": "1",
            "innerSchool": "1",
            "runDistance": runDistance,
            "runTime": runTime,
            "userId": userId,
            "vocalStatus": "1",
            "yearSemester": semesterYear,
            "recordDate" : getDate()
        }

        body = json.dumps(body)
        headers = {
            "token": token,
            "appKey": APPKEY,
            "sign": get_sign(None, body),
            "Content-Type": CONTENTTYPE,
            "User-Agent": USERAGENT
        }
        response = requests.post(HOST + "v1/unirun/save/run/record/new", headers=headers, data=body)
        data = response.json()
        msg = data["msg"]
        if data["code"] == 10000:
            resultDesc = data["response"]["resultDesc"]
            result = f"{studentName}: 跑步速度：{average:.2f}分钟/公里 跑步结果：{resultDesc}\n"
            return result
        else:
            return msg