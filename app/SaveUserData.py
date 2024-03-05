import json
import os
from collections import OrderedDict

def save_data(data):
    data_to_save = data.copy()
    data_to_save["token"] = data["oauthToken"]["token"]
    data_to_save["refreshToken"] = data["oauthToken"]["refreshToken"]
    del data_to_save["oauthToken"]

    # 加载已保存的用户数据
    saved_data = load_data()
    if saved_data is None:
        saved_data = []

    # 生成新的用户序号
    user_id = len(saved_data) + 1

    # 添加新的用户数据
    user_data = OrderedDict()
    user_data["id"] = user_id
    user_data["data"] = data_to_save
    saved_data.append(user_data)

    # 重新排序用户数据
    sorted_data = sorted(saved_data, key=lambda x: x["id"])

    with open('user_data.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f)

def load_data():
    try:
        if os.path.getsize('user_data.json') > 0:
            with open('user_data.json', 'r') as f:
                data = json.load(f)
                # 重新分配id值
                for i, item in enumerate(data, start=1):
                    item["id"] = i
            # 将修改后的数据写回文件
            with open('user_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)
            return data
        else:
            return []
    except FileNotFoundError:
        return []