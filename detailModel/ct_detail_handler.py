# coding=utf-8


"""
电信的通话相当获取
"""

import time
import json
import datetime
from . import hget_name
from . import hset_name
from . import DETAIL_URL
from . import DETAIL_HEADERS
from . import DETAIL_PAYLOADS
from . import cookie_dealer
from . import get_request
from . import post_request
from . import session_cookie_update
from . import cookie_transform
from . import save_new_cookie

# config
ID_KEY = ''
XCODE = 'ct'
URL_DICT = DETAIL_URL.get(XCODE)
HEADERS_DICT = DETAIL_HEADERS.get(XCODE)
PAYLOADS_DICT = DETAIL_PAYLOADS.get(XCODE)


def login_fare_detail_sys(url):
    cookies_list, cookies = cookie_dealer(ID_KEY)
    headers_sso = HEADERS_DICT.get('sso_headers')
    resp_sso = get_request(url=url, headers=headers_sso, cookies=cookies)
    if resp_sso:
        new_cookie = session_cookie_update(cookies_list, resp_sso.cookies.items())
        url_esc = resp_sso.headers.get('Location')
        headers_esc = HEADERS_DICT.get('esc_heades')
        cookie_esc = cookie_transform(new_cookie)
        resp_esc = get_request(url=url_esc, headers=headers_esc, cookies=cookie_esc)
        if resp_esc:
            new_cookie = session_cookie_update(cookies_list, resp_esc.cookies.items())
            url_ecsoot = resp_esc.headers.get('Location')
            headers_ecsoot = HEADERS_DICT.get('ecsoot_headers')
            cookie_ecsoot = cookie_transform(new_cookie)
            resp_ecsoot = get_request(url=url_ecsoot, headers=headers_ecsoot, cookies=cookie_ecsoot)
            if resp_ecsoot:
                new_cookie = session_cookie_update(cookies_list, resp_ecsoot.cookies.items())
                url_prov = resp_ecsoot.headers.get('Location')
                headers_prov = HEADERS_DICT.get('prov_headers')
                cookies_prov = cookie_transform(new_cookie)
                resp_prov = get_request(url=url_prov, headers=headers_prov, cookies=cookies_prov)
                if resp_prov:
                    new_cookie = session_cookie_update(cookies_list, resp_prov.cookies.items())
                    save_new_cookie(ID_KEY, new_cookie)


def check_my_session():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get('check_ss_url')
    headers = HEADERS_DICT.get('check_ss_headers')
    payloads = PAYLOADS_DICT.get('check_session')
    resp = post_request(url=url, headers=headers, data=payloads, cookies=cookies)
    if resp:
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        save_new_cookie(ID_KEY, new_cookie)


def send_mail_check_info():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    name = hget_name(ID_KEY, 'name')
    card = hget_name(ID_KEY, 'card')
    url_mail = URL_DICT.get('send_mail_url')
    headers_mail = HEADERS_DICT.get('mail_headers')
    payload_mail = PAYLOADS_DICT.get('payloads_mail')
    resp_mail = post_request(url=url_mail, headers=headers_mail, data=json.dumps(payload_mail), cookies=cookies)
    if resp_mail:
        new_cookie = session_cookie_update(cookies_list, resp_mail.cookies.items())
        code = input('\t请输入短信验证码:\t')
        hset_name(ID_KEY, 'captcha2', code)
        url_check = URL_DICT.get('check_url')
        headers_check = HEADERS_DICT.get('check_headers')
        payload_check = PAYLOADS_DICT.get('payloads_check').encode('utf-8') % (name, card, code)
        cookie_mail = cookie_transform(new_cookie)
        resp_check = post_request(url=url_check, headers=headers_check, data=payload_check, cookies=cookie_mail)
        if resp_check:
            new_cookie = session_cookie_update(cookies_list, resp_mail.cookies.items())
            save_new_cookie(ID_KEY, new_cookie)


def query_data():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url_query = URL_DICT.get('query_url')
    headers_query = HEADERS_DICT.get('query_headers')
    cookies_list.append(('s_sq', '%5B%5BB%5D%5D'))
    cookies = cookie_transform(cookies_list)
    data = []
    for i in range(6):
        current_month = (datetime.datetime.today() - datetime.timedelta(days=30*i)).strftime('%Y年%m月')
        payloads_query = (PAYLOADS_DICT.get('payloads_query').format(current_month)).encode('utf-8')
        resp_query = post_request(url=url_query, headers=headers_query, cookies=cookies, data=payloads_query)
        new_cookie = session_cookie_update(cookies_list, resp_query.cookies.items())
        data.append(resp_query.content.decode('utf-8'))
        save_new_cookie(ID_KEY, new_cookie)
        time.sleep(5)
    hset_name(ID_KEY, 'data', json.dumps(data))


def ct_detail_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    fare_link = hget_name(ID_KEY, 'ex2')
    detail_link = hget_name(ID_KEY, 'ex3')
    login_fare_detail_sys(fare_link)
    check_my_session()
    login_fare_detail_sys(detail_link)
    send_mail_check_info()
    query_data()
