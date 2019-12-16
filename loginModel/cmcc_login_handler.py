# coding=utf-8

"""
该模块为移动的登录模块
移动很淘气啊
服务端写入的cookie要按升序排列

12-16: 开始迭代
    针对登录过程中手机号是否验证
    验证失败的情况 返回相应的结果
    ** 目前看来移动是登录过程默认短信验证 **
    苦于没有其他手机号支撑
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


def get_args_maker(params) -> tuple:
    return URL_DICT.get(params), HEADERS_DICT.get(params), PARAMS_DICT.get(params)


def post_args_maker(params) -> tuple:
    return URL_DICT.get(params), HEADERS_DICT.get(params), PAYLOADS_DICT.get(params)


def general_request(name) -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get(name)
    headers = HEADERS_DICT.get(name)
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return


def ready_2_login() -> None:
    general_request(name='init_page')
    general_request(name='load_sendflag')
    general_request(name='captchazh')
    general_request(name='genqr')
    general_request(name='check_uid')
    return 


def check_number() -> None:
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('check_number')
    data.update({'userName': phone})
    resp = post_request(url=url, headers=headers, cookies=cookies, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return


def need_verify_code() -> str:
    result = '0'
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker('need_verify_code')
    params.update({'account': phone, 'timestamp': round(1000*time.time())})
    resp = get_request(url=url, headers=headers, cookies=cookies, params=params)
    if resp:
        js_dict = json_loads(resp.content.decode('utf-8'))
        result = js_dict.get('needVerifyCode')
    return result


def load_token() -> None:
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('load_token')
    data.update({'userName': phone})
    resp = post_request(url=url, headers=headers, cookies=cookies, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
        token = json.loads(resp.content.decode('utf-8')).get('result')
        hset_name(id_key=ID_KEY, field='ex1', value=token)
    return 


def send_code() -> None:
    phone = hget_name(id_key=ID_KEY, name='phone')
    token = hget_name(id_key=ID_KEY, name='ex1')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('send_code')
    headers.update({'Xa-before': token})
    data.update({'userName': phone})
    resp = post_request(url=url, headers=headers, cookies=cookies, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return


def send_flag() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker('send_flag')
    params.update({'timestamp': int(1000 * time.time())})
    resp = get_request(url=url, headers=headers, params=params, cookies=cookies)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return


def receive_mail_code() -> None:
    check_number()
    result = need_verify_code()
    load_token()
    if result == '1':
        send_code()
    send_flag()


def do_login() -> bool:
    phone = hget_name(id_key=ID_KEY, name='phone')
    pwd = hget_name(id_key=ID_KEY, name='pwd')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    # todo: 这里改为消息队列等待数据
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
        js_dict = json_loads(resp.content.decode('utf-8'))
        code = js_dict.get('code')
        if code == '0000':
            save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
            hset_name(id_key=ID_KEY, field='html', value=resp.content.decode('utf-8'))
            return True
        else:
            info = js_dict.get('desc')
            hset_name(id_key=ID_KEY, field='info', value=json.dumps(info))
            hset_name(id_key=ID_KEY, field='login', value=json.dumps(False))
    
    return False


def do_artifact() -> None:
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
                save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp_new.cookies.items()))
                hset_name(id_key=ID_KEY, field='login', value=json.dumps(True))
    return 


def cmcc_run(tkey) -> None:
    global ID_KEY
    ID_KEY = tkey
    ready_2_login()
    receive_mail_code()
    is_login = do_login()
    if is_login:
        do_artifact()
    return
