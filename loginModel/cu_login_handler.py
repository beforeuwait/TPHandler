# coding=utf-8


"""
该模块为联通的登录模块
"""

import time
import execjs
from . import N3FA_EXT
from . import DCSFPC
from . import N3FA_CID
from . import N3FA_LVT
from . import N3FA_LPVT
from . import PROV_LIST
from . import LOGIN_URL
from . import LOGIN_HEADERS
from . import LOGIN_PARAMS
from . import hget_name
from . import cookie_dealer
from . import session_cookie_update
from . import save_new_cookie
from . import cookie_transform
from . import get_request


# config
ID_KEY = ''
XCODE = 'cu'
URL_DICT = LOGIN_URL.get(XCODE)
HEADERS_DICT = LOGIN_HEADERS.get(XCODE)
PARAMS_DICT = LOGIN_PARAMS.get(XCODE)


def ready_login():
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url_login = URL_DICT.get('login_page')
    headers_login = HEADERS_DICT.get('login_page')
    resp_login = get_request(url=url_login, headers=headers_login, cookies=cookies)
    if resp_login:
        new_cookie = session_cookie_update(cookies_list, resp_login.cookies.items())
        cookies = cookie_transform(new_cookie)
        url_erwei = URL_DICT.get('er_wei').format(int(1000 * time.time()))
        headers_erwei = HEADERS_DICT.get('er_wei')
        resp_erwei = get_request(url=url_erwei, headers=headers_erwei, cookies=cookies)
        if resp_erwei:
            new_cookie = session_cookie_update(cookies_list, resp_login.cookies.items())
            cookies = cookie_transform(new_cookie)
            url_release = URL_DICT.get('check_release')
            headers_release = HEADERS_DICT.get('check_release')
            params_release = PARAMS_DICT.get('check_release')
            params_release.update({
                'callback': params_release.get('callback').format(int(1000 * time.time())),
                '_': int(1000 * time.time())})
            resp_release = get_request(url=url_release, headers=headers_release, params=params_release, cookies=cookies)
            if resp_release:
                new_cookie = session_cookie_update(new_cookie, resp_release.cookies.items())
                cookies = cookie_transform(new_cookie)
                url_verify = URL_DICT.get('check_verify')
                headers_verify = HEADERS_DICT.get('check_verify')
                params_verify = PARAMS_DICT.get('check_verify')
                call_back = params_verify.get('callback')
                params_verify.update({
                    'userName': phone,
                    'callback': call_back.format(int(1000 * time.time())),
                    '_': int(1000 * time.time())})
                resp_verify = get_request(url=url_verify, headers=headers_verify, cookies=cookies, params=params_release)
                if resp_verify:
                    new_cookie = session_cookie_update(new_cookie, resp_verify.cookies.items())
                    save_new_cookie(ID_KEY, new_cookie)


def receive_mail_login():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(id_key=ID_KEY, name='phone')
    url_mail = URL_DICT.get('send_mail')
    headers_mail = HEADERS_DICT.get('send_mail')
    params_mail = PARAMS_DICT.get('send_mail')
    params_mail.update({'callback': params_mail.get('callback').format(int(1000*time.time())),
                        'req_time': int(1000*time.time()),
                        'mobile': phone,
                        '_': int(1000*time.time())})
    resp_mail = get_request(url=url_mail, headers=headers_mail, params=params_mail, cookies=cookies)
    if resp_mail:
        new_cookie = session_cookie_update(cookies_list, resp_mail.cookies.items())
        cookies = cookie_transform(new_cookie)
        pwd = input('\t请输入短信验证码:\t')
        # todo: 当前遇到的情况是不需要验证码
        # todo: 添加一个需要验证码的
        url_log = URL_DICT.get('login')
        headers_log = HEADERS_DICT.get('login')
        params_log = PARAMS_DICT.get('login')
        params_log.update({
            'userName': phone,
            'password': pwd,
            'callback': params_log.get('callback').format(int(1000*time.time())),
            'req_time': int(1000*time.time()),
            '_': int(1000*time.time())})
        resp_log = get_request(url=url_log, headers=headers_log, cookies=cookies, params=params_log)
        if resp_log:
            new_cookie = session_cookie_update(new_cookie, resp_log.cookies.items())
            save_new_cookie(ID_KEY, new_cookie)


def init_login_cookie():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    prov = hget_name(id_key=ID_KEY, name='prov')
    prov_info = PROV_LIST.get(prov)
    cookies_demo = []
    ft = execjs.compile(N3FA_EXT).call('buildExt')
    cookies_demo.append(execjs.compile(DCSFPC).call('dcsFPC'))
    cookies_demo.append(['_n3fa_cid', execjs.compile(N3FA_CID).call('uuid')])
    cookies_demo.append(['_n3fa_ext', ft])
    cookies_demo.append([N3FA_LVT, ft.replace('ft=', '')])
    cookies_demo.append([N3FA_LPVT, ft.replace('ft=', '')])
    cookies_demo.append(['citycode', prov_info.get('cityCode')])
    cookies_demo.append(['userprocode', ''.join(['0', prov_info.get('provinceCode')])])
    cookies_demo.append(['mallcity', '{0}|{1}'.format(prov_info.get('provinceCode'), prov_info.get('cityCode'))])
    news_cookies = session_cookie_update(cookies_list, cookies_demo)
    save_new_cookie(ID_KEY, news_cookies)


def cu_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    init_login_cookie()
    ready_login()
    receive_mail_login()
