# coding=utf-8

"""
    该模块为电信的登录模块
"""

import re
from . import cookie_transform
from . import LOGIN_URL
from . import LOGIN_HEADERS
from . import get_request
from . import post_request
from . import save_new_cookie
from . import cookie_dealer
from . import session_cookie_update


# config
XCODE = 'ct'
URL_DICT = LOGIN_URL.get(XCODE)
HEADERS_DICT = LOGIN_HEADERS.get(XCODE)


def request_first_cookie(id_key):
    url = URL_DICT.get('first_request')
    headers = HEADERS_DICT.get('origin')
    cookies_list, cookies = cookie_dealer(id_key)
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        city_code = resp.content.decode('utf-8')
        cookies_list.extend(resp.cookies.items())
        cookies_list.append(('cityCode', city_code))
        save_new_cookie(id_key, cookies_list)
    return


def request_2nd_home_page(id_key):
    url = URL_DICT.get('home_page')
    headers = HEADERS_DICT.get('origin')
    cookies_list, cookies = cookie_dealer(id_key)
    resp = get_request(url=url, headers=headers)
    if resp:
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        save_new_cookie(id_key, new_cookie)


def request_log_index(id_key):
    """
    请求拿到的登录的url
    :return:
    """
    url = URL_DICT.get('login_index')
    headers = HEADERS_DICT.get('login_index')
    cookies_list, cookies = cookie_dealer(id_key)
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        login_url = re.findall('loginUrl":"(.*?)"', resp.content.decode('utf-8'))
        if login_url:
            new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
            save_new_cookie(id_key, new_cookie)
            return ''.join(['http://www.189.cn', login_url[0]])
        else:
            return


def request_login_url(id_key, url):
    """
    请求网页返回的页面，获取cookie
    请求会发生跳转，然后写入关键cookie
    :return:
    """
    cookies_list, cookies = cookie_dealer(id_key)
    headers = HEADERS_DICT.get('login_index')
    resp = get_request(url=url, headers=headers)
    if resp:
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        save_new_cookie(id_key, new_cookie)


def ct_run(id_key):
    request_first_cookie(id_key)
    request_2nd_home_page(id_key)
    login_url = request_log_index(id_key)
    request_login_url(id_key, login_url)