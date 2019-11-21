# coding=utf-8


"""
    针对三大运营商的通话详情数据获取模块
    这里仅仅是一个demo
    感兴趣的，获取别的数据都行
    哪怕通过爬虫修改自己的套餐都行

"""

from .config import DETAIL_URL
from .config import DETAIL_HEADERS
from .config import DETAIL_PAYLOADS
from utils import hget_name
from utils import hset_name
from utils import cookie_dealer
from utils import cookie_transform
from utils import get_request
from utils import post_request
from utils import session_cookie_update
from utils import save_new_cookie
from .ct_detail_handler import ct_detail_run


def receive_key_do_switcher(id_key):
    """
    这里作为一个转换器，获取id_key然后开始执行登录部分
    :param id_key:  一开始通过md5计算出来的值
    :return:
    """
    sp = hget_name(id_key, 'sp')
    # 执行逻辑
    sp_switcher(sp)(id_key)


def sp_switcher(sp):
    sp_dict = {
        'cmcc': '',
        'ct': ct_detail_run,
        'cu': ''
    }
    return sp_dict.get(sp)