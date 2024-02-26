import hashlib

def string_to_md5(plain_text: str) -> str:
    m = hashlib.md5()
    m.update(plain_text.encode('utf-8'))
    md5code = m.hexdigest().lower()
    return md5code
