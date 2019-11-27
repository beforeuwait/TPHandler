# coding=utf-8

# url

DETAIL_URL = {
        'cmcc': {
        'loginfo': 'https://shop.10086.cn/i/v1/auth/loginfo',
        'home': 'https://shop.10086.cn/i/?f=home',
        'sso': 'https://login.10086.cn/SSOCheck.action?channelID=12003&backUrl=https://shop.10086.cn/i/?f=home',
        'showvec': 'https://shop.10086.cn/i/apps/serviceapps/billdetail/showvec.html',
        'capt_img': 'https://shop.10086.cn/i/authImg',
        'capt_check': 'https://shop.10086.cn/i/v1/res/precheck/{0}',
        'mail': 'https://shop.10086.cn/i/v1/fee/detbillrandomcodejsonp/{0}',
        'final': 'https://shop.10086.cn/i/v1/fee/detailbilltempidentjsonp/{0}',
        'detail': 'https://shop.10086.cn/i/v1/fee/detailbillinfojsonp/{0}',
    },
    'cu': {},
    'ct': {
        'send_mail_url': 'https://sc.189.cn/cloudapi/UnionSendsmsTemplateDeatil/UnionSendsmsTemplateDeatil',
        'check_url': 'https://sc.189.cn/cloudapi/QryDeatil/checkCode',
        'query_url': 'https://sc.189.cn/cloudapi/QryDeatil/QryDeatilNew',
        'check_ss_url': 'http://www.189.cn/dqmh/my189/checkMy189Session.do',
    }
}


# headers

DETAIL_HEADERS = {
    'cmcc': {
        'loginfo': {
            'Host': 'shop.10086.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-store, must-revalidate',
            'pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Content-Type': '*',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'If-Modified-Since': '0',
            'expires': '0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://shop.10086.cn/i/?f=billdetailqry',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        },
        'home': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'sso': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'artifact': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'wel': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'showvec': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'capt_img': {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        },
        'capt_check': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-store, must-revalidate',
            'Connection': 'keep-alive',
            'Content-Type': '*',
            'expires': '0',
            'Host': 'shop.10086.cn',
            'If-Modified-Since': '0',
            'pragma': 'no-cache',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'mail': {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': '*',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'final': {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': '*',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'detail': {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': '*',
            'Host': 'shop.10086.cn',
            'Referer': 'https://shop.10086.cn/i/?f=home',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
    },
    'cu': {},
    'ct': {
        'sso_headers': {
            'Host': 'www.189.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'http://www.189.cn/dqmh/my189/initMy189home.do?fastcode=20000326',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive'
        },
        'esc_heades': {
            'Host': 'www.189.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'http://www.189.cn/dqmh/my189/initMy189home.do?fastcode=20000326',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive'
        },
        'ecsoot_headers': {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'nested-navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-site',
            'Referer': 'https://www.189.cn/dqmh/my189/initMy189home.do',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        },
        'prov_headers': {
            'Host': 'sc.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'nested-navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-site',
            'Referer': 'https://www.189.cn/dqmh/my189/initMy189home.do',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        },
        'mail_headers': {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'Content-Type': 'application/json',
            'Host': 'sc.189.cn',
            'Origin': 'https://sc.189.cn',
            'Referer': 'https://sc.189.cn/cloud/static/templates/deatil-query.html?fastcode=20000326&cityCode=sc',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'check_headers': {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'Content-Type': 'application/json',
            'Host': 'sc.189.cn',
            'Origin': 'https://sc.189.cn',
            'Referer': 'https://sc.189.cn/cloud/static/templates/deatil-query.html?fastcode=20000326&cityCode=sc',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'query_headers': {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '50',
            'Content-Type': 'application/json',
            'Host': 'sc.189.cn',
            'Origin': 'https://sc.189.cn',
            'Referer': 'https://sc.189.cn/cloud/static/templates/deatil-query.html?fastcode=20000326&cityCode=sc',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'check_ss_headers': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Content-Length': '17',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.189.cn',
            'Origin': 'http://www.189.cn',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.189.cn/dqmh/my189/initMy189home.do?fastcode=20001054',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
    }
}

# 请求参数

DETAIL_PAYLOADS = {
    'cmcc': {},
    'cu': {},
    'ct': {
        'check_session': '{"fastcode": "20000326"}',
        'payloads_mail': {"body": {}},
        'payloads_check': {"body": {"name": "", "idcard": "", "code": ""}},
        'payloads_query': '{"body": {"qryType": "21", "qryDate": "%s"}}'
    }
}

DETAIL_PARAMS = {
    'cmcc': {
        'loginfo': {
            '_': '',    # 时间戳
        },
        'capt_img': {
            't': '',    # 时间戳
        },
        'capt_check': {
            'captchaVal': '',   # 验证码
            '_': '',    # 时间戳
        },
        'mail': {
            'callback': 'jQuery05385169086723893_1573457132131',
            '_': '',    # 时间戳
        },
        'final': {
            'callback': 'jQuery05385169086723893_1573457132131',
            'pwdTempSerCode': '',
            'pwdTempRandCode': '',
            'captchaVal': '',
            '_': '',    # 时间戳
        },
        'detail': {
            'callback': 'jQuery05385169086723893_1573457132131',
            'curCuror': '1',
            'step': '100',
            'qryMonth': '', # 查询时间
            'billType': '02',
            '_': '',    # 时间戳
        }
    },
    'cu': {},
    'ct': {}
}