# coding=utf-8

"""
惹不起的联通

会用cookie下毒

在登录前按照以往的写法，没问题
登陆后，cookie 要么是 dict格式，要么放headers里 才行
"""

import time
import requests
from config import LOGIN_URL
from config import LOGIN_HEADERS
from config import LOGIN_PARAMS
from config import LOGIN_PAYLOADS
from config import URL_DETAIL
from config import HEADERS_DETAIL
from config import PARAMS_DETAIL
from config import PAYLOADS_DETAIL


ss = requests.Session()
# config
URL_DICT = LOGIN_URL
HEADERS_DICT = LOGIN_HEADERS
PARAMS_DICT = LOGIN_PARAMS
PAYLOADS_DICT = LOGIN_PAYLOADS


def general_request(name):
    """通用的请求"""
    url = URL_DICT.get(name)
    headers = HEADERS_DICT.get(name)
    ss.get(url=url, headers=headers, verify=False)


def general_request_params(name):
    url = URL_DICT.get(name)
    headers = HEADERS_DICT.get(name)
    params = LOGIN_PARAMS.get(name)
    params.update({'callback': params.get('callback').format(int(1000*time.time())), '_': int(1000*time.time())})
    ss.get(url=url, headers=headers, params=params, verify=False)


def search_per_info():
    url = URL_DICT.get('searchPerInfo')
    headers = HEADERS_DICT.get('searchPerInfo')
    data = PAYLOADS_DICT.get('searchPerInfo')
    data.update({'_': int(1000*time.time())})
    ss.post(url=url, headers=headers, data=data, verify=False)


def search_per_info_user():
    url = URL_DICT.get('searchPerInfoUser')
    headers = HEADERS_DICT.get('searchPerInfoUser')
    data = PAYLOADS_DICT.get('searchPerInfoUser')
    data.update({'_': int(1000*time.time())})
    ss.post(url=url, headers=headers, data=data, verify=False)


def check_login():
    url = URL_DICT.get('checklogin').format(int(1000*time.time()))
    headers = HEADERS_DICT.get('checklogin')
    ss.post(url=url, headers=headers, verify=False)


def get_js():
    url = URL_DICT.get('getJs').format(int(1000*time.time()), int(1000*time.time()))
    headers = HEADERS_DICT.get('getJs')
    ss.get(url=url, headers=headers, verify=False)


def check_login_2():
    url = URL_DICT.get('checklogin2').format(int(1000*time.time()))
    headers = HEADERS_DICT.get('checklogin2')
    data = PAYLOADS_DICT.get('checklogin2')
    ss.post(url=url, headers=headers, data=data, verify=False)


def info():
    url = URL_DICT.get('info').format(int(1000*time.time()))
    headers = HEADERS_DICT.get('info')
    ss.post(url=url, headers=headers, verify=False)


def shopping():
    url = URL_DICT.get('shopping')
    headers = HEADERS_DICT.get('shopping')
    params = PARAMS_DICT.get('shopping')
    params.update({'callback': params.get('callback').format(int(1000*time.time())), '_': int(1000*time.time())})
    ss.get(url=url, headers=headers, params=params, verify=False)


def query_navigations():
    url = URL_DICT.get('QueryNavigations')
    headers = HEADERS_DICT.get('QueryNavigations')
    data = PAYLOADS_DICT.get('QueryNavigations')
    ss.post(url=url, headers=headers, data=data, verify=False)


def get_area_by_ip():
    url = URL_DICT.get('getAreaByIp').format(int(1000*time.time()))
    headers = HEADERS_DICT.get('getAreaByIp')
    ss.post(url=url, headers=headers, verify=False)


def check_need_verify(phone):
    url = URL_DICT.get('CheckNeedVerify')
    headers = HEADERS_DICT.get('CheckNeedVerify')
    params = PARAMS_DICT.get('CheckNeedVerify')
    params.update({'callback': params.get('callback').format(int(1000*time.time())), 'userName': phone, '_': int(1000*time.time())})
    resp = ss.get(url=url, headers=headers, params=params, verify=False)
    print(resp.content.decode('utf-8'))


def send_ck_msg(phone):
    url = URL_DICT.get('SendCkMSG')
    headers = HEADERS_DICT.get('SendCkMSG')
    params = PARAMS_DICT.get('SendCkMSG')
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   'mobile': phone,
                   '_': int(1000*time.time()),
                   'req_time': int(1000*time.time())})
    resp = ss.get(url=url, headers=headers, params=params, verify=False)
    print(resp.content.decode('utf-8'))


def mall_login(phone, pwd, code):
    url = URL_DICT.get('MallLogin')
    headers = HEADERS_DICT.get('MallLogin')
    params = PARAMS_DICT.get('MallLogin')
    params.update({'callback': params.get('callback').format(int(1000*time.time())),
                   'req_time': int(1000*time.time()),
                   'userName': phone,
                   'password': pwd,
                   'verifyCKCode': code,
                   '_': int(1000*time.time())})
    resp = ss.get(url=url, headers=headers, params=params, verify=False)
    print(resp.content.decode('utf-8'))


def main_logic():
    phone = '185xxxxx785'
    pwd = '45xxxx'
    general_request('call_dan_iframe')
    general_request('e4avatar_upload')
    general_request_params('getHeadImg')
    search_per_info()
    search_per_info_user()
    general_request('custLogin')
    check_login()
    general_request('call_dan')
    get_js()
    check_login_2()
    check_login_2()
    info()
    shopping()
    query_navigations()
    get_area_by_ip()
    check_need_verify(phone)
    send_ck_msg(phone)
    code = input('请输入验证码........:')
    mall_login(phone, pwd, code)


def common():
    url = URL_DETAIL.get('common')
    headers = HEADERS_DETAIL.get('common')
    ss.post(url=url, headers=headers)


def after_login():
    common()
    general_request('call_dan_iframe')
    general_request_params('getHeadImg')
    search_per_info()
    search_per_info_user()
    check_login()

if __name__ == '__main__':
    main_logic()
    after_login()