# coding=utf-8


LOGIN_URL = {
    'call_dan_iframe': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
    'e4avatar_upload': 'https://iservice.10010.com/e4/jsonp/e4avatar_upload.html',
    'getHeadImg': 'https://uac.10010.com/portal/Service/getHeadImg',
    'searchPerInfo': 'https://iservice.10010.com/e3/static/query/searchPerInfo/',
    'searchPerInfoUser': 'https://iservice.10010.com/e3/static/query/searchPerInfoUser/',
    'pageList': 'https://iservice.10010.com/e3/static/query/message/pageList',
    'checklogin': 'https://iservice.10010.com/e3/static/check/checklogin/?_={0}',
    'custLogin': 'https://uac.10010.com/portal/custLogin',
    'call_dan': 'https://iservice.10010.com/e4/query/bill/call_dan.html?menuId=000100030001',
    'getJs': 'https://iservice.10010.com/e3/static/transact/getJs?_={0}?_={1}&accessURL=https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
    'checklogin2': 'https://www.10010.com/mall/service/check/checklogin/?_={0}',
    'info': 'https://iservice.10010.com/e3/static/common/info?_={0}',
    'shopping': 'https://iservice.10010.com/e3/static/shopping/g',
    'QueryNavigations': 'https://www.10010.com/mall/service/query/QueryNavigations',
    'getAreaByIp': 'https://www.10010.com/mall/service/ipAddress/getAreaByIp/?_={0}',
    'CheckNeedVerify': 'https://uac.10010.com/portal/Service/CheckNeedVerify',
    'SendCkMSG': 'https://uac.10010.com/portal/Service/SendCkMSG',
    'MallLogin': 'https://uac.10010.com/portal/Service/MallLogin',
}


LOGIN_HEADERS = {
    'call_dan_iframe': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'iservice.10010.com',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    },
    'e4avatar_upload': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'nested-navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    },
    'getHeadImg': {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'uac.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    },
    'searchPerInfo': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'iservice.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'searchPerInfoUser': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'iservice.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'pageList': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'checklogin': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'iservice.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'custLogin': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'uac.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'nested-navigate',
        'Sec-Fetch-Site': 'same-site',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    },
    'call_dan': {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'getJs': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'iservice.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'checklogin2': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '18',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    },
    'info': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'iservice.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'shopping': {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'QueryNavigations': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '30',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'www.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    },
    'getAreaByIp': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    },
    'CheckNeedVerify': {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'uac.10010.com',
        'Referer': 'https://uac.10010.com/portal/custLogin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'SendCkMSG': {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'uac.10010.com',
        'Referer': 'https://uac.10010.com/portal/custLogin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },
    'MallLogin': {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'uac.10010.com',
        'Referer': 'https://uac.10010.com/portal/custLogin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
}

LOGIN_PARAMS = {
    'getHeadImg': {
        'callback': 'jQuery1123011424774332753085_{}',
        '_': ''
    },

    'pageList': {
        '_': '',
        'currentPage': '1',
        'pageSize': '2'
    },
    'shopping': {
        'callback': 'jQuery1123011424774332753085_{0}',
        '_': ''
    },
    'CheckNeedVerify': {
        'callback': 'jQuery17203665895120244169_{0}',
        'userName': '',
        'pwdType': '01',
        '_': ''
    },
    'SendCkMSG': {
        'callback': 'jQuery17203665895120244169_{0}',
        'req_time': '',
        'mobile': '',
        '_': ''
    },
    'MallLogin': {
        'callback': 'jQuery17203665895120244169_{0}',
        'req_time': '',
        'redirectURL': 'http://www.10010.com',
        'userName': '18582481785',
        'password': '',
        'pwdType': '01',
        'productType': '01',
        'redirectType': '06',
        'rememberMe': '1',
        'verifyCKCode': '',
        '_': ''
    }
}

LOGIN_PAYLOADS = {
    'searchPerInfo': {
        '_': ''
    },
    'searchPerInfoUser': {
        '_': ''
    },
    'checklogin2': {
        'jutThird': '',
        '_uop_id': ''
    },
    'QueryNavigations': {
        'jutThird': '',
        '_uop_id': '',
        'procode': '011'
    }
}

# ..................................................................

URL_DETAIL = {
    'common': 'https://iservice.10010.com/e3/static/common/l?_={0}',
}

HEADERS_DETAIL = {
    'common': {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'iservice.10010.com',
        'Origin': 'https://iservice.10010.com',
        'Referer': 'https://iservice.10010.com/e4/query/bill/call_dan-iframe.html',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    },

}

PARAMS_DETAIL = {

}


PAYLOADS_DETAIL = {}
