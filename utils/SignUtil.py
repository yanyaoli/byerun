import hashlib
import urllib.parse
from app.AppConfig import APPKEY, APPSECRET
from collections import OrderedDict

def get_sign(query, body):
    sign_str = ""
    if query is not None:
        # 将 query 的值转换为字符串
        sorted_query = OrderedDict(sorted(query.items()))
        sign_str = "".join([str(k) + str(v) for k, v in sorted_query.items()])
    # 追加APPKEY和APPSECRET
    sign_str += APPKEY
    sign_str += APPSECRET
    # 追加请求体
    if body is not None:
        sign_str += body

    replaced = False
    for ch in [" ", "~", "!", "(", ")", "'"]:
        if ch in sign_str:
            sign_str = sign_str.replace(ch, "")
            replaced = True

    if replaced:
        sign_str = urllib.parse.quote(sign_str)

    m = hashlib.md5()
    m.update(sign_str.encode('utf-8'))
    sign = m.hexdigest().upper()

    if replaced:
        sign += "encodeutf8"

    return sign