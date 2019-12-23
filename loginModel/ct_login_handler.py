# coding=utf-8

"""
    该模块为电信的登录模块
"""

import re
import time
import execjs
from . import cookie_transform
from . import hset_name
from . import LOGIN_URL
from . import LOGIN_HEADERS
from . import get_request
from . import post_request
from . import json_loads
from . import save_new_cookie
from . import cookie_dealer
from . import cookie_dealer_sorted
from . import session_cookie_update
from . import TRKID_JS
from . import CODE_V
from . import LVID_JS
from . import S_FID_JS
from . import NVID
from . import SVID_URL
from . import SVID_HEADERS
from . import SVID_PARAMS
from . import TRKHMCLICKCOORDS
from . import hget_name
from . import LOGIN_PAYLOADS
from . import LOGIN_PARAMS
from . import ASE
from . import ECS_REQINFO_LOGIN1
from PIL import Image

# config
ID_KEY = ''
XCODE = 'ct'
URL_DICT = LOGIN_URL.get(XCODE)
HEADERS_DICT = LOGIN_HEADERS.get(XCODE)
PAYLOADS_DICT = LOGIN_PAYLOADS.get(XCODE)
PARAMS_DICT = LOGIN_PARAMS.get(XCODE)


def request_first_cookie() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get('first_request')
    headers = HEADERS_DICT.get('origin')
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        cookies_list.append(('cityCode', resp.content.decode('utf-8')))
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return


def request_2nd_home_page() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get('home_page')
    headers = HEADERS_DICT.get('origin')
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def request_log_index() -> None:
    cookies_list, cookies = cookie_dealer_sorted(ID_KEY)
    url = URL_DICT.get('login_index')
    headers = HEADERS_DICT.get('login_index')
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        login_url = re.findall('loginUrl":"(.*?)"', resp.content.decode('utf-8'))
        if login_url:
            save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
            hset_name(id_key=ID_KEY, field='ex1', value=''.join(['http://www.189.cn', login_url[0]]))
    return


def request_login_url() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = hget_name(id_key=ID_KEY, name='ex1')
    headers = HEADERS_DICT.get('login_index')
    resp = get_request(url=url, headers=headers, cookies=cookies)
    if resp:
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        url_location_1 = resp.headers.get('Location')
        cookies = cookie_transform(new_cookie)
        resp_loc_1 = get_request(url=url_location_1, headers=headers, cookies=cookies)
        if resp_loc_1:
            new_cookie = session_cookie_update(cookies_list, resp_loc_1.cookies.items())
            cookies = cookie_transform(new_cookie)
            url_location_2 = resp_loc_1.headers.get('Location')
            resp_loc_2 = get_request(url=url_location_2, headers=headers, cookies=cookies)
            if resp_loc_2:
                save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp_loc_2.cookies.items()))


def add_cookie() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    trkid = execjs.compile(TRKID_JS).call('trkid_js')
    cookies_list.append(("kid", trkid))
    cookies_list.append(("code_v", CODE_V))
    lvid = execjs.compile(LVID_JS).call('lvid')
    cookies_list.append(("lvid", lvid))
    s_fid = execjs.compile(S_FID_JS).call('s_fid')
    cookies_list.append(("s_fid", s_fid))
    cookies_list.append(("nvid", NVID))
    SVID_PARAMS.update({'fid': s_fid, 'c17': trkid})
    cookies = cookie_transform(cookies_list)
    resp = get_request(url=SVID_URL, headers=SVID_HEADERS, params=SVID_PARAMS, cookies=cookies)
    if resp:
        cookies_list.append(("trkHmClickCoords", TRKHMCLICKCOORDS))
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))


def check_phone_number() -> bool:
    is_contuine = True
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(ID_KEY, 'phone')
    url = URL_DICT.get('check_phone')
    headers = HEADERS_DICT.get('check_phone')
    payloads_1 = PAYLOADS_DICT.get('check_payloads_1')
    payloads_2 = PAYLOADS_DICT.get('check_payloads_2')
    payloads_1.update({'phone': phone})
    resp_1 = post_request(url=url, headers=headers, data=payloads_1, cookies=cookies)
    if resp_1:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp_1.cookies.items()))
        js_dict = json_loads(resp_1.content)
        if js_dict:
            p_id = js_dict.get('provinceId')
            payloads_2.update({'account': phone, 'ProvinceID': p_id})
            resp_2 = post_request(url=url, headers=headers, data=payloads_2, cookies=cookies)
            hset_name(id_key=ID_KEY, field='ex2', value=p_id)
            if resp_2:
                js_dict_2 = json_loads(resp_2.content.decode('utf-8'))
                if js_dict_2:
                    rsp_code = js_dict_2.get('rspCode')
                    if rsp_code != '0000':
                        hset_name(id_key=ID_KEY, field='info', value=js_dict_2.get('desc'))
                        is_contuine = False
                    else:  
                        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp_2.cookies.items()))
            else:
                hset_name(id_key=ID_KEY, field='info', value='手机号验证未通过')
                is_contuine = False
        else:
            hset_name(id_key=ID_KEY, field='info', value='手机号验证未通过')
            is_contuine = False
    return is_contuine


def request_captcha() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    url = URL_DICT.get('captcha')
    headers = HEADERS_DICT.get('captcha_headers')
    params = PARAMS_DICT.get('captcha_params')
    resp = get_request(url=url, headers=headers, params=params, cookies=cookies)
    img_name = './captchaImgs/ct_captcha_{0}.png'.format(int(time.time()))
    with open(img_name, 'wb') as f:
        f.write(resp.content)
    Image.open(img_name).show()
    captcha = input('\t手动输入图片验证码:')
    new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
    save_new_cookie(ID_KEY, new_cookie)
    hset_name(id_key=ID_KEY, field='captcha1', value=captcha)
    return


def mail_verify() -> bool:
    is_contuine = True
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(ID_KEY, 'phone')
    captcha = hget_name(ID_KEY, 'captcha1')
    p_id = hget_name(id_key=ID_KEY, name='ex2')
    url = URL_DICT.get('mail_verify')
    headers = HEADERS_DICT.get('mail_verify')
    payloads = PAYLOADS_DICT.get('login_mail')
    payloads.update({'account': phone, 'pid': p_id, 'captcha': captcha.upper()})
    resp = post_request(url=url, headers=headers, data=payloads, cookies=cookies)
    if resp:
        js_dict = json_loads(resp.content.decode('utf-8'))
        if js_dict:
            rsp_code = js_dict.get('rspCode')
            if rsp_code != '0000':
                hset_name(id_key=ID_KEY, field='info', value=js_dict.get('desc'))
                is_contuine = False
            else:
                save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return is_contuine


def mail_code_deal() -> None:
    mail_captcha = input('\t请输入短信验证码:')
    pwd = execjs.compile(ASE).call('ase', mail_captcha)
    hset_name(ID_KEY, 'pwd', pwd)
    return


def validate_login() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(ID_KEY, 'phone')
    pwd = hget_name(ID_KEY, 'pwd')
    url = URL_DICT.get('validate_url')
    headers = HEADERS_DICT.get('validate_headers')
    payloads = PAYLOADS_DICT.get('vaildate_payloads')
    payloads.update({'uName': phone, 'uPwd': pwd})
    resp = post_request(url=url, headers=headers, cookies=cookies, data=payloads)
    if resp:
        save_new_cookie(ID_KEY, session_cookie_update(cookies_list, resp.cookies.items()))
    return 


def e_r_login1_maker() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(ID_KEY, 'phone')
    p_id = hget_name(ID_KEY, 'ex2')
    ctx = '{0}$$201$地市（中文/拼音）${1}$$$0'.format(phone, p_id)
    erl_1 = execjs.compile(ASE).call('login1', ctx)
    cookies_list.append((ECS_REQINFO_LOGIN1, erl_1))
    save_new_cookie(ID_KEY, cookies_list)
    return 


def login_get_html() -> bool:
    is_continue = True
    cookies_list, cookies = cookie_dealer(ID_KEY)
    phone = hget_name(ID_KEY, 'phone')
    pwd = hget_name(ID_KEY, 'pwd')
    captcha = hget_name(ID_KEY, 'captcha1')
    p_id = hget_name(ID_KEY, 'ex2')
    url = URL_DICT.get('login')
    headers = HEADERS_DICT.get('login_headers')
    payloads = PAYLOADS_DICT.get('login_payloads')
    payloads.update({'Account': phone, 'ProvinceID': p_id, 'Captcha': captcha, 'Password': pwd})
    resp = post_request(url=url, headers=headers, data=payloads, cookies=cookies)
    if resp:
        location_url = resp.headers.get('Location')
        if not location_url:
            hset_name(id_key=ID_KEY, field='info', value='短信验证码错误或者其他导致登录失败')
            is_continue = False
            return is_continue
        new_cookie = session_cookie_update(cookies_list, resp.cookies.items())
        cookies = cookie_transform(new_cookie)
        headers = HEADERS_DICT.get('ecs_headers')
        resp_location_1 = get_request(url=location_url, headers=headers, cookies=cookies)
        if resp_location_1:
            new_cookie = session_cookie_update(new_cookie, resp_location_1.cookies.items())
            cookies = cookie_transform(new_cookie)
            location_url_2 = resp_location_1.headers.get('Location')
            resp_location_2 = get_request(url=location_url_2, headers=headers, cookies=cookies)
            if resp_location_2:
                save_new_cookie(ID_KEY, session_cookie_update(new_cookie, resp_location_2.cookies.items()))
                html = resp_location_2.content.decode('utf-8')
                hset_name(id_key=ID_KEY, field='html', value=html)
    return is_continue


def do_redirect_get_cloud_session() -> None:
    cookies_list, cookies = cookie_dealer(ID_KEY)
    html = hget_name(ID_KEY, 'html')
    headers = HEADERS_DICT.get('redirect_headers')
    link = re.findall('src="/dqmh/ssoLink.do\?(.*?)"', html, re.S)[0]
    url = ''.join(['http://www.189.cn/dqmh/ssoLink.do?', link])
    resp_1 = get_request(url=url, headers=headers, cookies=cookies)
    if resp_1:
        new_cookie = session_cookie_update(cookies_list, resp_1.cookies.items())
        url_2 = resp_1.headers.get('Location')
        cookies = cookie_transform(new_cookie)
        resp_2 = get_request(url=url_2, headers=headers, cookies=cookies)
        if resp_2:
            new_cookie = session_cookie_update(new_cookie, resp_2.cookies.items())
            url_3 = resp_2.headers.get('Location')
            cookies = cookie_transform(new_cookie)
            resp_3 = get_request(url=url_3, headers=headers, cookies=cookies)
            if resp_3:
                new_cookie = session_cookie_update(new_cookie, resp_3.cookies.items())
                url_4 = resp_3.headers.get('Location')
                cookies = cookie_transform(new_cookie)
                headers_prov = HEADERS_DICT.get('each_prov_headers')
                headers_prov.update({'Host': 'sc.189.cn'})
                resp_4 = get_request(url=url_4, headers=headers_prov, cookies=cookies)
                if resp_4:
                    new_cookie = session_cookie_update(new_cookie, resp_4.cookies.items())
                    url_5 = resp_4.headers.get('Location')
                    cookies = cookie_transform(new_cookie)
                    headers_prov = HEADERS_DICT.get('each_prov_headers')
                    resp_5 = get_request(url=url_5, header=headers_prov, cookies=cookies)
                    if resp_5:
                        new_cookie = session_cookie_update(new_cookie, resp_5.cookies.items())
                        url_user = URL_DICT.get('user_page')
                        headers_home = HEADERS_DICT.get('user_headers')
                        cookies = cookie_transform(new_cookie)
                        resp_home = get_request(url=url_user, headers=headers_home, cookies=cookies)
                        if resp_home:
                            save_new_cookie(ID_KEY, session_cookie_update(new_cookie, resp_home.cookies.items()))
                            fare_link = '/dqmh/ssoLink.do?method=linkTo&platNo=10023&toStUrl=https://sc.189.cn/cloud/static/templates/fare-search.html?fastcode=20001054&cityCode=sc'
                            detail_link = re.findall('gotoIfremBody\(\'(.*?)\',\'20000326', resp_home.content.decode('utf-8'))[0]
                            hset_name(ID_KEY, 'ex3', ''.join(['http://www.189.cn', fare_link]))
                            hset_name(ID_KEY, 'ex4', ''.join(['http://www.189.cn', detail_link]))


def ct_run(tkey):
    global ID_KEY
    ID_KEY = tkey
    request_first_cookie()
    request_2nd_home_page()
    request_log_index()
    request_login_url()
    add_cookie()
    is_contuine = check_phone_number()
    if not is_contuine:
        return
    request_captcha()
    is_contuine = mail_verify()
    if not is_contuine:
        return
    mail_code_deal()
    validate_login()
    e_r_login1_maker()
    is_contuine = login_get_html()
    if not is_contuine:
        return
    do_redirect_get_cloud_session()
