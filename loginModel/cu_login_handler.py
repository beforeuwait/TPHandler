# coding=utf-8


"""
该模块为联通的登录模块

12-12: 更新新的登陆模块
从接受验证登录，改为使用密码登录，同时接收验证码
登陆后，仍然需要短信验证
然后可以采集数据了
联通的数据比较奇葩， 一次20条，出现翻页的情况
"""


import time
from . import LOGIN_URL
from . import LOGIN_HEADERS
from . import LOGIN_PARAMS
from . import LOGIN_PAYLOADS
from . import hget_name
from . import hset_name
from . import cookie_dealer
from . import session_cookie_update
from . import save_new_cookie
from . import get_request_cu
from . import post_request_cu


# config
ID_KEY = ''
XCODE = 'cu'
URL_DICT = LOGIN_URL.get(XCODE)
HEADERS_DICT = LOGIN_HEADERS.get(XCODE)
PARAMS_DICT = LOGIN_PARAMS.get(XCODE)
PAYLOADS_DICT = LOGIN_PAYLOADS.get(XCODE)


def get_args_maker(params):
    return URL_DICT.get(params), HEADERS_DICT.get(params), PARAMS_DICT.get(params)


def post_args_maker(params):
    return URL_DICT.get(params), HEADERS_DICT.get(params), PAYLOADS_DICT.get(params)


def general_request(name):
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker(name)
    headers.update(cookies)
    resp = get_request_cu(url=url, headers=headers)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def general_request_params(name):
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker(name)
    headers.update(cookies)
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   '_': int(1000*time.time())})
    resp = get_request_cu(url=url, headers=headers, params=params)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def search_per_info():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('search_per_info')
    headers.update(cookies)
    data.update({'_': int(1000*time.time())})
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def search_per_info_user():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('search_per_info_user')
    headers.update(cookies)
    data.update({'_': int(1000*time.time())})
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def check_login():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('checklogin')
    url = URL_DICT.get('checklogin').format(int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def get_js():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('get_js')
    url = URL_DICT.get('get_js').format(int(1000*time.time()), int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def check_login_2():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('checklogin2')
    url = URL_DICT.get('checklogin2').format(int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def info():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('info')
    url = URL_DICT.get('info').format(int(1000 * time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def shopping():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker('shopping')
    headers.update(cookies)
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   '_': int(1000*time.time())})
    resp = get_request_cu(url=url, headers=headers, params=params)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def query_navigations():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('query_navigations')
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def get_area_by_ip():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('get_area_by_ip')
    url = url.format(int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def check_need_verify():
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker('check_need_verify')
    headers.update(cookies)
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   'userName': phone,
                   '_': int(1000*time.time())})
    resp = get_request_cu(url=url, headers=headers, params=params)
    if resp:
        # todo:这里添加一个验证过程
        # 如果不验证的情况，直接登录
        # 如果验证的情况，接受短信登录
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def send_ck_msg():
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker('send_ck_msg')
    headers.update(cookies)
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   'mobile': phone,
                   '_': int(1000*time.time()),
                   'req_time': int(1000*time.time())})
    resp = get_request_cu(url=url, headers=headers, params=params)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return


def deal_code():
    code = input('请输入验证码........:')
    hset_name(id_key=ID_KEY, field='captcha1', value=code)
    return


def mall_login():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(id_key=ID_KEY, name='phone')
    pwd = hget_name(id_key=ID_KEY, name='pwd')
    code = hget_name(id_key=ID_KEY, name='captcha1')
    url, headers, params = get_args_maker('mall_login')
    headers.update(cookies)
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   'req_time': int(1000*time.time()),
                   'userName': phone,
                   'password': pwd,
                   'verifyCKCode': code,
                   '_': int(1000*time.time())})
    resp = get_request_cu(url=url, headers=headers, params=params)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def cu_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    general_request('call_dan_iframe')
    general_request('e4avatar_upload')
    general_request_params('get_head_img')
    search_per_info()
    search_per_info_user()
    general_request('cust_login')
    check_login()
    general_request('call_dan')
    get_js()
    check_login_2()
    check_login_2()
    info()
    shopping()
    query_navigations()
    get_area_by_ip()
    check_need_verify()
    send_ck_msg()
    deal_code()
    mall_login()
