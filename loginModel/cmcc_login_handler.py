# coding=utf-8

"""
该模块为移动的登录模块
移动很淘气啊
服务端写入的cookie要按升序排列

12-16: 开始迭代
    针对登录过程中手机号是否验证
    验证失败的情况 返回相应的结果
"""


import time
import json
from . import get_request
from . import post_request
from . import LOGIN_URL
from . import LOGIN_HEADERS
from . import LOGIN_PAYLOADS
from . import LOGIN_PARAMS
from . import cookie_dealer
from . import session_cookie_update
from . import save_new_cookie
from . import hget_name
from . import cookie_transform
from . import encrpt_pwd
from . import hset_name
from . import json_loads


# config
ID_KEY = ''
XCODE = 'cmcc'
URL_DICT = LOGIN_URL.get(XCODE)
HEADERS_DICT = LOGIN_HEADERS.get(XCODE)
PAYLOADS_DICT = LOGIN_PAYLOADS.get(XCODE)
PARAMS_DICT = LOGIN_PARAMS.get(XCODE)


def ready_2_login():
    general_request(param='init_page')
    general_request(param='load_sendflag')
    general_request(param='captchazh')
    general_request(param='genqr')
    general_request(param='check_uid')


def receive_mail_code():
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url_check = URL_DICT.get('check_number')
    headers_check = HEADERS_DICT.get('check_number')
    data_check = PAYLOADS_DICT.get('check_number')
    data_check.update({'userName': phone})
    resp_check = post_request(url=url_check, headers=headers_check, cookies=cookies, data=data_check)
    if resp_check:
        new_cookie = session_cookie_update(cookies_list, resp_check.cookies.items())
        cookies = cookie_transform(new_cookie)
        url_token = URL_DICT.get('load_token')
        headers_token = HEADERS_DICT.get('load_token')
        data_token = PAYLOADS_DICT.get('load_token')
        data_token.update({'userName': phone})
        resp_token = post_request(url=url_token, headers=headers_token, cookies=cookies, data=data_token)
        if resp_token:
            token = json.loads(resp_token.content.decode('utf-8')).get('result')
            new_cookie = session_cookie_update(new_cookie, resp_token.cookies.items())
            cookies = cookie_transform(new_cookie)
            url_code = URL_DICT.get('send_code')
            headers_code = HEADERS_DICT.get('send_code')
            headers_code.update({'Xa-before': token})
            data_code = PAYLOADS_DICT.get('send_code')
            data_code.update({'userName': phone})
            resp_code = post_request(url=url_code, headers=headers_code, data=data_code, cookies=cookies)
            if resp_code:
                new_cookie = session_cookie_update(new_cookie, resp_code.cookies.items())
                cookies = cookie_transform(new_cookie)
                url_flag = URL_DICT.get('send_flag')
                headers_flag = HEADERS_DICT.get('send_flag')
                params_flag = PARAMS_DICT.get('send_flag')
                params_flag.update({'timestamp': int(1000 * time.time())})
                resp_flag = get_request(url=url_flag, headers=headers_flag, params=params_flag, cookies=cookies)
                if resp_flag:
                    new_cookie = session_cookie_update(cookies_list, resp_code.cookies.items())
                    save_new_cookie(ID_KEY, new_cookie)


def do_login():
    phone = hget_name(id_key=ID_KEY, name='phone')
    pwd = hget_name(id_key=ID_KEY, name='pwd')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    captcha_code = input('请输入短信验证码:\t')
    url = URL_DICT.get('login')
    headers = HEADERS_DICT.get('login')
    params = PARAMS_DICT.get('login')
    params.update({'account': phone,
                         'password': encrpt_pwd(pwd),
                         'smsPwd': captcha_code,
                         'timestamp': int(1000*time.time())
                         })
    resp = get_request(url=url, headers=headers, params=params, cookies=cookies)
    if resp:
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        save_new_cookie(ID_KEY, new_cookie)
        hset_name(id_key=ID_KEY, field='html', value=resp.content.decode('utf-8'))
    return


def do_artifact():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    html = hget_name(id_key=ID_KEY, name='html')
    js_dict = json_loads(html)
    if js_dict:
        artifact = js_dict.get('artifact')
        url_artifact = js_dict.get('assertAcceptURL')
        headers_artifact = HEADERS_DICT.get('artifact')
        params_artifact = PARAMS_DICT.get('artifact')
        params_artifact.update({'artifact': artifact})
        resp_arti = get_request(url=url_artifact, headers=headers_artifact, params=params_artifact, cookies=cookies)
        if resp_arti:
            new_cookie = session_cookie_update(cookies_list, resp_arti.cookies.items())
            url_location = resp_arti.headers.get('Location')
            cookies = cookie_transform(new_cookie)
            resp_new = get_request(url=url_location, headers=headers_artifact, cookies=cookies)
            if resp_new:
                new_cookie = session_cookie_update(cookies_list, resp_new.cookies.items())
                save_new_cookie(ID_KEY, new_cookie)


def general_request(param):
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get(param)
    headers = HEADERS_DICT.get(param)
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        save_new_cookie(ID_KEY, new_cookie)


def cmcc_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    ready_2_login()
    receive_mail_code()
    do_login()
    do_artifact()
    return
