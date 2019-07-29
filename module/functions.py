import hashlib
import json


def pwd(password):
    salt = "doubleStar.."
    password = salt + hashlib.md5(password.encode(encoding='UTF-8')).hexdigest() + salt
    password = salt + hashlib.md5(password.encode(encoding='UTF-8')).hexdigest() + salt
    return hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()


# json返回
def return_json(code, message):
    jsons = {
        "code": code,
        "message": message
    }
    return json.dumps(jsons)


def return_jsons(code, data):
    jsons = {
        "code": code,
        "data": data
    }
    return json.dumps(jsons)
