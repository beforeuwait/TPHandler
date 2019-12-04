# coding=utf-8


"""
    程序的入口
    传入参数为 手机号 服务密码 运营商 身份证号
    起手计算一个身份id 为 手机号+时间戳 的md5码
"""

import time
from utils import calculate_md5
from utils import hmset_data
from loginModel import receive_key_do_switcher as login_switch
from detailModel import receive_key_do_switcher as detail_switch


def run(init_data):
    id_key = calculate_md5('_'.join([init_data.get('phone'), str(int(1000*time.time()))]))
    push_2_redis(id_key, init_data)
    login_switch(id_key)
    detail_switch(id_key)


def transform_sp(sp):
    switcher = {
        '移动': 'cmcc',
        '电信': 'ct',
        '联通': 'cu'
    }
    return switcher.get(sp)


def push_2_redis(id_key, map_data):
    map_data.update({'cookies': '',
                     'captcha1': '',
                     'captcha2': '',
                     'sp': transform_sp(map_data.get('sp')),
                     'html': '',
                     'ex1': '',
                     'ex2': '',
                     'ex3': '',
                     'data': ''})
    hmset_data(id_key, map_data)
    return


if __name__ == '__main__':
    data = {
        'phone': '182xxxxxx30',
        'name': '',
        'pwd': '1xxxx3',
        'card': '511xxxxxxxxxxxx4',
        'sp': '移动'
    }
    data2 = {
        'phone': '199xxxxxx084',
        'name': 'xxx',
        'pwd': '',
        'card': '511xxxxxxxxxxxx4',
        'sp': '电信'
    }
    data3 = {
        'phone': '185xxxxxx85',
        'pwd': '',
        'name': '',
        'card': '511xxxxxxxxxxxx4',
        'sp': '联通',
        'prov': '四川'
    }
    run(data3)

