# coding=utf-8


import json
import time
import requests
from login_model import login_main_logic
from login_model import general_request
from login_model import general_request_params
from login_model import search_per_info
from login_model import search_per_info_user
from login_model import check_login
from login_model import get_area_by_ip
from login_model import info
from login_model import get_js
from login_model import shopping
from login_model import query_navigations
from config import DETAIL_URL
from config import DETAIL_HEADERS
from config import DETAIL_PARAMS
from config import DETAIL_PAYLOADS


#
ss = requests.Session()

URL_DICT = DETAIL_URL
HEADERS_DICT = DETAIL_HEADERS
PARAMS_DICT = DETAIL_PARAMS
PAYLOADS_DICT = DETAIL_PAYLOADS


def common():
    url = URL_DICT.get('common')
    headers = HEADERS_DICT.get('common')
    ss.post(url=url, headers=headers, verify=False)


def page_list():
    url = URL_DICT.get('pageList')
    headers = HEADERS_DICT.get('pageList')
    params = PARAMS_DICT.get('pageList')
    params.update({'_': int(1000*time.time())})
    ss.get(url=url, headers=headers, params=params, verify=False)


def verification_sms():
    url = URL_DICT.get('verificationSms').format(int(1000*time.time()), int(1000*time.time()))
    headers = HEADERS_DICT.get('verificationSms')
    data = PAYLOADS_DICT.get('verificationSms')
    ss.post(url=url, headers=headers, data=data, verify=False)


def limit_query_collector():
    url = URL_DICT.get('limitQueryCollector')
    headers = HEADERS_DICT.get('limitQueryCollector')
    ss.post(url=url, headers=headers, verify=False)


def page_list_2(phone):
    url = URL_DICT.get('pageList2')
    headers = HEADERS_DICT.get('pageList2')
    data = PAYLOADS_DICT.get('pageList2')
    data.update({'usernumber': phone})
    ss.post(url=url, headers=headers, data=data, verify=False)


def checkmap_extra_param():
    url = URL_DICT.get('checkmapExtraParam').format(int(1000*time.time()))
    headers = HEADERS_DICT.get('checkmapExtraParam')
    data = PAYLOADS_DICT.get('checkmapExtraParam')
    ss.post(url=url, headers=headers, data=data, verify=False)


def send_random_code():
    url = URL_DICT.get('sendRandomCode').format(int(1000*time.time()), int(1000*time.time()))
    headers = HEADERS_DICT.get('sendRandomCode')
    data = PAYLOADS_DICT.get('sendRandomCode')
    ss.post(url=url, headers=headers, data=data, verify=False)


def verification_submit(code):
    url = URL_DICT.get('verificationSubmit').format(int(1000*time.time()), int(1000*time.time()))
    headers = HEADERS_DICT.get('verificationSubmit')
    data = PAYLOADS_DICT.get('verificationSubmit')
    data.update({'inputcode': code})
    ss.post(url=url, headers=headers, data=data, verify=False)


def call_detail():
    url = URL_DICT.get('callDetail').format(int(1000*time.time()), int(1000*time.time()))
    headers = HEADERS_DICT.get('callDetail')
    data = PAYLOADS_DICT.get('callDetail')
    resp = ss.post(url=url, headers=headers, data=data, verify=False)
    print(resp.content.decode('utf-8'))


def detail_main_logic():
    phone = '185xxxxxx85'
    pwd = 'xxxxxx'
    cookie_object = login_main_logic(phone, pwd)
    ss.cookies.update(cookie_object)
    common()
    general_request('call_dan_iframe')
    general_request_params('getHeadImg')
    search_per_info()
    search_per_info_user()
    page_list()
    check_login()
    info()
    general_request('call_dan')
    get_js()
    verification_sms()
    info()
    shopping()
    query_navigations()
    limit_query_collector()
    page_list_2(phone)
    check_login()
    checkmap_extra_param()
    get_area_by_ip()
    print('sleep 10 seconds.......')
    time.sleep(10)
    send_random_code()
    code = input('请输入短信验证码.............')
    verification_submit(code)
    call_detail()


if __name__ == '__main__':
    detail_main_logic()