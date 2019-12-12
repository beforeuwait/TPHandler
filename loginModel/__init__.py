# coding=utf-8

"""该模块承担的是
移动，电信，联通
的登录逻辑模块

**目前仅仅支持四川**
# ###########################
# ###### cmcc代表 中国移动 ##
# ###### cu代表 中国联通 ##
# ###### ct代表 中国电信 ####
# ##########################

每一次请求进来，颁发一个身份证，cookie信息都存储在redis对应的身份证里
这样做的目的在于，对于放到线上接口且高并发的情况下不容易错
身份证为 手机号+时间戳 进行md5转换
"""


import requests
from utils import cookie_transform
from utils import connect_redis
from utils import hset_name
from utils import get_request
from utils import post_request
from utils import get_request_cu
from utils import post_request_cu
from utils import save_new_cookie
from utils import cookie_dealer
from utils import hget_name
from utils import session_cookie_update
from utils import json_loads
from utils import encrpt_pwd
from .config import PROV_LIST
from .config import LOGIN_URL
from .config import LOGIN_HEADERS
from .config import LOGIN_PARAMS
from .config import LOGIN_PAYLOADS
from .js_hacker import TRKID_JS
from .js_hacker import CODE_V
from .js_hacker import LVID_JS
from .js_hacker import S_FID_JS
from .js_hacker import NVID
from .js_hacker import TRKHMCLICKCOORDS
from .js_hacker import SVID_URL
from .js_hacker import SVID_HEADERS
from .js_hacker import SVID_PARAMS
from .js_hacker import ECS_REQINFO_LOGIN1
from .js_hacker import ASE
from .js_hacker import DCSFPC
from .js_hacker import N3FA_CID
from .js_hacker import N3FA_EXT
from .js_hacker import N3FA_LVT
from .js_hacker import N3FA_LPVT
from .ct_login_handler import ct_run
from .cmcc_login_handler import cmcc_run
from .cu_login_handler import cu_run


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
        'cmcc': cmcc_run,
        'ct': ct_run,
        'cu': cu_run,
    }
    return sp_dict.get(sp)
