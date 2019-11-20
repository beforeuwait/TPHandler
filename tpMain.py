# coding=utf-8


"""
    程序的入口
    传入参数为 手机号 服务密码 运营商 身份证号
    起手计算一个身份id 为 手机号+时间戳 的md5码
"""

import time
from utils import calculate_md5
from utils import hmset_data
from loginModel import receive_key_do_switcher


def run(init_data):
    # 初始化原始数据
    id_key = calculate_md5('_'.join([init_data.get('phone'), str(int(1000*time.time()))]))
    push_2_redis(id_key, init_data)
    receive_key_do_switcher(id_key)


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
                     'ex3': ''})
    hmset_data(id_key, map_data)
    return


if __name__ == '__main__':
    data = {
        'phone': '182xxxxxxxxxx',
        'pwd': '112233',
        'card': '511xxxxxxxxxxxx034',
        'sp': '移动'
    }
    data2 = {
        'phone': '181xxxxxxxxxx',
        'pwd': '',
        'card': '511xxxxxxxxxxxx034',
        'sp': '电信'
    }
    data3 = {
        'phone': '185xxxxxxxxx85',
        'pwd': '',
        'card': '511xxxxxxxxxxxx034',
        'sp': '联通'
    }
    run(data2)
