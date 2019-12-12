# coding=utf-8

"""
该模块为联通的详单查询部分
"""

import time
import json
import datetime
from . import json_loads
from . import hget_name
from . import hset_name
from . import DETAIL_URL
from . import DETAIL_HEADERS
from . import DETAIL_PARAMS
from . import DETAIL_PAYLOADS
from . import cookie_dealer
from . import get_request_cu
from . import post_request_cu
from . import session_cookie_update
from . import save_new_cookie


# config
ID_KEY = ''
XCODE = 'cu'
URL_DICT = DETAIL_URL.get(XCODE)
HEADERS_DICT = DETAIL_HEADERS.get(XCODE)
PARAMS_DICT = DETAIL_PARAMS.get(XCODE)
PAYLOADS_DICT = DETAIL_PAYLOADS.get(XCODE)


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


def judge_days_in_month(month: int, year: int):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return '31'
    elif month in (4, 6, 9, 11):
        return '30'
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return '29'
        else:
            return '28'


def common():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('common')
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers)
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


def page_list():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, params = get_args_maker('page_list')
    headers.update(cookies)
    params.update({'_': int(1000*time.time())})
    resp = get_request_cu(url=url, headers=headers, params=params)
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


def info():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('info')
    url = URL_DICT.get('info').format(int(1000 * time.time()))
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


def verification_sms():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('verification_sms')
    url = url.format(int(1000*time.time()), int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers, data=data)
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


def limit_query_collector():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('limit_query_collector')
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def page_list_2():
    phone = hget_name(id_key=ID_KEY, name='phone')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('page_list2')
    headers.update(cookies)
    data.update({'usernumber': phone})
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def checkmap_extra_param():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('checkmap_extra_param')
    url = url.format(int(1000*time.time()))
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


def send_random_code():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('send_random_code')
    url = url.format(int(1000*time.time()), int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def deal_code():
    code = input('请输入验证码........:')
    hset_name(id_key=ID_KEY, field='captcha2', value=code)
    return


def verification_submit():
    code = hget_name(id_key=ID_KEY, name='captcha2')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('verification_submit')
    url = url.format(int(1000*time.time()), int(1000*time.time()))
    headers.update(cookies)
    data.update({'inputcode': code})
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def call_detail():
    """
    # 测试用只获取一次数据
    # 联通的数据返回存在翻页的情况
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('call_detail')
    url = url.format(int(1000*time.time()), int(1000*time.time()))
    headers.update(cookies)
    resp = post_request_cu(url=url, headers=headers, data=data)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
        data = resp.content.decode('utf-8')
        hset_name(id_key=ID_KEY, field='data', value=json.dumps(data))
    """
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url, headers, data = post_args_maker('call_detail')
    current_date = datetime.datetime.today()
    data_list = []
    for i in range(6):
        n, pages = 1, 1
        while n <= pages:
            order_date = current_date - datetime.timedelta(days=30*i)
            st = ''.join([current_date.strftime('%Y%m'), '01'])
            if i == 0:
                ed = current_date.strftime('%Y%m%d')
            else:
                ed = judge_days_in_month(int(order_date.strftime('%m')), int(order_date.strftime('%Y')))
            data.update({
                'beginDate': st,
                'endDate': ed
            })
            resp = post_request_cu(url=url, headers=headers, data=data)
            if resp:
                save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
                html = resp.content.decode('utf-8')
                data_list.append(html)
                js_dict = json_loads(html)
                pages = js_dict.get('pageMap').get('totalPages')
            n += 1
            # 休眠3秒
            time.sleep(3)
    hset_name(id_key=ID_KEY, field='data', value=json.dumps(data_list))


def cu_detail_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    common()
    general_request('call_dan_iframe')
    general_request_params('get_head_img')
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
    page_list_2()
    check_login()
    checkmap_extra_param()
    get_area_by_ip()
    print('sleep 10 seconds.......')
    time.sleep(10)
    send_random_code()
    deal_code()
    verification_submit()
    call_detail()
