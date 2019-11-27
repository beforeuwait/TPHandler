# coding=utf-8


"""
该模块为移动的详单获取模块
"""


import json
import time
import execjs
import random
import base64
import datetime
from . import hset_name
from . import hget_name
from . import get_request
from . import DETAIL_URL
from . import DETAIL_HEADERS
from . import DETAIL_PAYLOADS
from . import DETAIL_PARAMS
from . import cookie_dealer
from . import session_cookie_update
from . import cookie_transform
from . import save_new_cookie
from . import COLLECT_ID
from . import WTFPC
from PIL import Image


# config
ID_KEY = ''
XCODE = 'cmcc'
URL_DICT = DETAIL_URL.get(XCODE)
HEADERS_DICT = DETAIL_HEADERS.get(XCODE)
PAYLOADS_DICT = DETAIL_PAYLOADS.get(XCODE)
PARAMS_DICT = DETAIL_PARAMS.get(XCODE)


def init_bill_page():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url_loginfo = URL_DICT.get('loginfo')
    headers_loginfo = HEADERS_DICT.get('loginfo')
    params_loginfo = PARAMS_DICT.get('loginfo')
    params_loginfo.update({'_': int(1000*time.time())})
    resp_loginfo = get_request(url=url_loginfo, headers=headers_loginfo, params=params_loginfo, cookies=cookies)
    if resp_loginfo:
        new_cookie = session_cookie_update(cookies_list, resp_loginfo.cookies.items())
        url_home = URL_DICT.get('home')
        headers_home = HEADERS_DICT.get('home')
        cookies = cookie_transform(new_cookie)
        resp_home = get_request(url=url_home, headers=headers_home, cookies=cookies)
        if resp_home:
            new_cookie = session_cookie_update(new_cookie, resp_loginfo.cookies.items())
            params_loginfo.update({'_': int(1000*time.time())})
            cookies = cookie_transform(new_cookie)
            resp_loginfo2 = get_request(url=url_loginfo, headers=headers_loginfo, params=params_loginfo, cookies=cookies)
            if resp_loginfo2:
                url_sso = URL_DICT.get('sso')
                headers_sso = HEADERS_DICT.get('sso')
                cookies = cookie_transform(new_cookie)
                resp_sso = get_request(url=url_sso, headers=headers_sso, cookies=cookies)
                if resp_sso:
                    new_cookie = session_cookie_update(new_cookie, resp_sso.cookies.items())
                    url_arti = resp_sso.headers.get('Location')
                    headers_arti = HEADERS_DICT.get('artifact')
                    cookies = cookie_transform(new_cookie)
                    resp_arti = get_request(url=url_arti, headers=headers_arti, cookies=cookies)
                    if resp_arti:
                        new_cookie = session_cookie_update(new_cookie, resp_arti.cookies.items())
                        url_wel = resp_arti.headers.get('Location')
                        headers_wel = HEADERS_DICT.get('wel')
                        cookies = cookie_transform(new_cookie)
                        resp_wel = get_request(url=url_wel, headers=headers_wel, cookies=cookies)
                        if resp_wel:
                            new_cookie = session_cookie_update(new_cookie, resp_wel.cookies.items())
                            save_new_cookie(ID_KEY, new_cookie)


def update_cookie():
    cookies_list, cookies = cookie_dealer(ID_KEY)
    cookies_list.append(('collect_id', get_collect_id()))
    cookies_list.append(('WT_FPC', get_wtfpc()))
    return


def set_random_num():
    hset_name(id_key=ID_KEY, field='ex1', value=str(random.random()).replace('.', ''))
    return


def visit_detail_page():
    phone = hget_name(id_key=ID_KEY, name='phone')
    pwd = hget_name(id_key=ID_KEY, name='pwd')
    rdm = hget_name(id_key=ID_KEY, name='ex1')
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url_showvec = URL_DICT.get('showvec')
    headers_showvec = HEADERS_DICT.get('showvec')
    resp_showvec = get_request(url=url_showvec, headers=headers_showvec, cookies=cookies)
    if resp_showvec:
        new_cookie = session_cookie_update(cookies_list, resp_showvec.cookies.items())
        url_capt = URL_DICT.get('capt_img')
        headers_capt = HEADERS_DICT.get('capt_img')
        params_capt = PARAMS_DICT.get('capt_img')
        params_capt.update({'t': int(1000*time.time())})
        cookies = cookie_transform(new_cookie)
        resp_capt = get_request(url=url_capt, headers=headers_capt, params=params_capt, cookies=cookies)
        if resp_capt:
            new_cookie = session_cookie_update(new_cookie, resp_capt.cookies.items())
            cookies = cookie_transform(new_cookie)
            img_name = './captchaImgs/cmcc_captcha_{0}.png'.format(int(time.time()))
            with open(img_name, 'wb') as f:
                f.write(resp_capt.content)
            Image.open(img_name).show()
            capt = input('\t手动输入图片验证码:')
            url_check = URL_DICT.get('capt_check').format(phone)
            headers_check = HEADERS_DICT.get('capt_check')
            params_check = PARAMS_DICT.get('capt_check')
            params_check.update({'captchaVal': capt, '_': int(1000*time.time())})
            resp_check = get_request(url=url_check, headers=headers_check, params=params_check, cookies=cookies)
            if resp_check:
                new_cookie = session_cookie_update(new_cookie, resp_check.cookies.items())
                cookies = cookie_transform(new_cookie)
                print('为了等短信60秒。。。。。。。')
                time.sleep(60)
                print('开始请求短信')
                url_mail = URL_DICT.get('mail').format(phone)
                headers_mail = HEADERS_DICT.get('mail')
                params_mail = PARAMS_DICT.get('mail')
                params_mail.update({
                    'callback': ''.join(["jQuery", rdm, '_', str(int(1000*time.time()))]),
                    '_': int(1000*time.time())}
                    )
                resp_mail = get_request(url=url_mail, headers=headers_mail, cookies=cookies, params=params_mail)
                print(resp_mail.content.decode('utf-8'))
                if resp_mail:
                    new_cookie = session_cookie_update(new_cookie, resp_mail.cookies.items())
                    cookies = cookie_transform(new_cookie)
                    # 通过最后验证
                    random_pwd = input('请输入短信验证码:\t')
                    url_final = URL_DICT.get('final').format(phone)
                    headers_final = HEADERS_DICT.get('final')
                    params_final = PARAMS_DICT.get('final')
                    params_final.update({
                        'callback': ''.join(["jQuery", rdm, '_', str(int(1000 * time.time()))]),
                        'pwdTempSerCode': base64.b64encode(pwd.encode()),
                        'pwdTempRandCode': base64.b64encode(random_pwd.encode()),
                        'captchaVal': capt,
                        '_': int(time.time())
                        })
                    resp_final = get_request(url=url_final, headers=headers_final, params=params_final, cookies=cookies)
                    if resp_final:
                        new_cookie = session_cookie_update(new_cookie, resp_mail.cookies.items())
                        save_new_cookie(ID_KEY, new_cookie)


def get_detail():
    phone = hget_name(id_key=ID_KEY, name='phone')
    rdm = hget_name(id_key=ID_KEY, name='ex1')
    data = []
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get('detail').format(phone)
    headers = HEADERS_DICT.get('detail')
    params = PARAMS_DICT.get('detail')
    current_date = datetime.datetime.today()
    for i in range(6):
        querry_date = (current_date - datetime.timedelta(days=30)).strftime('%Y%m')
        params.update({
            'callback': ''.join(["jQuery", rdm, '_', str(int(1000 * time.time()))]),
            'qryMonth': querry_date,
            '_': int(1000*time.time())
        })
        resp = get_request(url=url, headers=headers, params=params, cookies=cookies)
        data.append(resp.content.decode('utf-8'))
    hset_name(id_key=ID_KEY, field='data', value=json.dumps(data))


def get_collect_id():
    return execjs.compile(COLLECT_ID).call('cid')


def get_wtfpc():
    return execjs.compile(WTFPC).call('wtfpc')


def cmcc_detail_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    init_bill_page()
    update_cookie()
    set_random_num()
    visit_detail_page()
    get_detail()