# coding=utf-8

# url

DETAIL_URL = {
    'cmcc': {},
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
    'cmcc': {},
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
        'payloads_check': '{"body": {"name": "%s", "idcard": "%s", "code":"%s"}}',
        'payloads_query': '{"body": {"qryType": "21", "qryDate": "%s"}}'
    }
}