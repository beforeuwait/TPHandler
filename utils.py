# coding=utf-8

import requests
import json
import hashlib
from redis import StrictRedis

# 屏蔽warning
requests.packages.urllib3.disable_warnings()


# json 处理
def json_loads(js_ctx):
    js_dict = None
    try:
        js_dict = json.loads(js_ctx)
    except:
        print('json加载出错',js_ctx)
    return js_dict

# cookie编辑
def cookie_transform(c_l):
    return {"Cookie": ';'.join(['='.join([c[0], str(c[1])])for c in c_l])}


# 请求模块
def get_request(**kwargs):
    retry = 5
    resp = None
    while retry > 0:
        try:
            resp = requests.get(url=kwargs.get('url'),
                                headers=kwargs.get('headers'),
                                cookies=kwargs.get('cookies'),
                                params=kwargs.get('params'),
                                verify=False,
                                allow_redirects=False)
            if resp.status_code <= 302:
                break
        except Exception as e:
            pass
        retry -= 1
    return resp


def post_request(**kwargs):
    retry = 5
    resp = None
    while retry > 0:
        try:
            resp = requests.post(url=kwargs.get('url'),
                                 headers=kwargs.get('headers'),
                                 cookies=kwargs.get('cookies'),
                                 data=kwargs.get('data'),
                                 verify=False,
                                 allow_redirects=False)
            if resp.status_code <= 302:
                break
        except Exception as e:
            pass
        retry -= 1
    return resp


# 创建一个session管理器
def session_cookie_update(origin, new_cookie):
    # 模拟session的cookie管理
    # 主要目的是去重以及输出items
    cookie = {}
    for key, value in origin:
        cookie[key] = value
    # 开始更新
    for new_key, new_value in new_cookie:
        cookie.update({new_key: new_value})
    return [(k, v) for k, v in cookie.items()]


# 链接redis
# keywords
HOST = "localhost"
PORT = 6379
DB = 3
PHONE = 'phone'
PWD = 'pwd'
CARD = 'card'
COOKIE = 'cookies'
CAPTCHA1 = 'captcha1'
CAPTCHA2 = 'captcha2'


def connect_redis():
    return StrictRedis(host=HOST, port=PORT, db=DB)


def hmset_data(id_key, data_dict):
    """
    向redis放入
    key        field value field value field value field value  field   value field  value field value
    id_number   phone xxxx  cookie xxxx  card xxxx   pwd  xxxxx  captcha1 xx  captcha2  xx  sp   cmcc
    每个 key的有效期为 600秒
    """
    rds = connect_redis()
    rds.hmset(name=id_key, mapping=data_dict)
    rds.expire(name=id_key, time=600)


def hset_name(id_key, field, value):
    rds = connect_redis()
    rds.hset(name=id_key, key=field, value=value)


def hget_name(id_key, name):
    rds = connect_redis()
    return rds.hget(name=id_key, key=name).decode()


def get_current_cookie(id_key):
    cookie_str = hget_name(id_key, COOKIE)
    if cookie_str:
        cookie_dict = json.loads(cookie_str)
        if isinstance(cookie_dict, list):
            return cookie_dict
    return []


def save_new_cookie(id_key, new_cookies):
    return hset_name(id_key, COOKIE, json.dumps(new_cookies, ensure_ascii=False))


# 计算md5
def calculate_md5(ctx):
    m = hashlib.md5(ctx.encode())
    return m.hexdigest()


# cookie_deal
def cookie_dealer(id_key):
    cookies_list = get_current_cookie(id_key)
    cookies = cookie_transform(cookies_list)
    return cookies_list, cookies

