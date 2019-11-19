# coding=utf-8

# ###########################
# ###### 10086代表 中国移动 ##
# ###### 10010代表 中国联通 ##
# ###### 189代表 中国电信 ####
# ##########################


# url

LOGIN_URL = {
    '10086': {
        'init_page': 'https://login.10086.cn/login.html',
        'load_sendflag': 'https://login.10086.cn/loadSendflag.htm?timestamp=',
        'captchazh': 'https://login.10086.cn/captchazh.htm?type=12',
        'genqr': 'https://login.10086.cn/genqr.htm',
        'check_uid': 'https://login.10086.cn/checkUidAvailable.action',
        'check_number': 'https://login.10086.cn/chkNumberAction.action',
        'load_token': 'https://login.10086.cn/loadToken.action',
        'send_code': 'https://login.10086.cn/sendRandomCodeAction.action',
        'send_flag': 'https://login.10086.cn/sendflag.htm',
        'login': 'https://login.10086.cn/login.htm'
    },
    '10010': {
        'home_page': 'http://www.10010.com/net5/{0}/',
        'hall_url': 'http://uac.10010.com/portal/hallLogin',
        'login_page': 'https://uac.10010.com/portal/homeLoginNew',
        'check_verify': 'https://uac.10010.com/portal/Service/CheckNeedVerify',
        'send_mail': 'https://uac.10010.com/portal/Service/SendMSG',
        'login': 'https://uac.10010.com/portal/Service/MallLogin',
        'er_wei': 'https://uac.10010.com/oauth2/genqr?timestamp={0}',
        'check_release': 'https://uac.10010.com/portal/Service/checkRelease',
    },
    '189': {
        'first_request': 'http://www.189.cn/dqmh/system.do?operate=index',
        'home_page': 'http://www.189.cn',
        'login_index': 'http://www.189.cn/login/index.do',
        'check_phone': 'https://login.189.cn/web/login/ajax',
        'captcha': 'https://login.189.cn/web/captcha',
        'mail_verify': 'https://login.189.cn/web/login/ajax',
        'validate_url': 'https://login.189.cn/web/pwd/validate',
        'login': 'https://login.189.cn/web/login',
        'user_page': 'https://www.189.cn/dqmh/my189/initMy189home.do'
    }
}


# headers

LOGIN_HEADERS = {
    '10086': {
        'init_page': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        },
        'load_sendflag': {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        },
        'captchazh': {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        },
        'genqr': {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        },
        'check_uid': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'login.10086.cn',
            'Origin': 'https://login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'check_number': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '49',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'login.10086.cn',
            'Origin': 'https://login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'load_token': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '20',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'login.10086.cn',
            'Origin': 'https://login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'send_code': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '44',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'login.10086.cn',
            'Origin': 'https://login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Xa-before': '',        # token 需要添加
        },
        'send_flag': {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        },
        'login': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'artifact': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www1.10086.cn',
            'Referer': 'https://login.10086.cn/login.html',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        },
    },
    '10010': {
        'login_page': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'uac.10010.com',
            'Referer': 'https://uac.10010.com/portal/mallLogin.jsp?redirectURL=http://www.10010.com/net5/',
            'Sec-Fetch-Mode': 'nested-navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        },
        'check_verify': {
            'Host': 'uac.10010.com',
            'Connection': 'keep-alive',
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://uac.10010.com/portal/homeLoginNew',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        },
        'send_mail': {
            'Host': 'uac.10010.com',
            'Connection': 'keep-alive',
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://uac.10010.com/portal/homeLoginNew',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        },
        'login': {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'uac.10010.com',
            'Referer': 'https://uac.10010.com/portal/homeLoginNew',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'er_wei': {
            'Host': 'uac.10010.com',
            'Connection': 'keep-alive',
            'Sec-Fetch-Mode': 'no-cors',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://uac.10010.com/portal/homeLoginNew',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        },
        'check_release': {
            'Host': 'uac.10010.com',
            'Connection': 'keep-alive',
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://uac.10010.com/portal/mallLogin.jsp?redirectURL=http://www.10010.com/net5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        },
    },
    '189': {
        'origin': {
            'Host': 'www.189.cn',
            'Content-Length': '0',
            'Origin': 'http://www.189.cn',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'http://www.189.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive'
            },
        'login_index': {
            'Host': 'www.189.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'http://www.189.cn/html/login/index.html',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive'
        },
        'check_phone': {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Content-Length': '30',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://login.189.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        },
        'captcha_headers': {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'login.189.cn',
            'Referer': 'https://login.189.cn/web/login',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        },
        'mail_verify': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '64',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'login.189.cn',
            'Origin': 'https://login.189.cn',
            'Referer': 'https://login.189.cn/web/login',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        },
        'validate_headers': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '78',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'login.189.cn',
            'Origin': 'https://login.189.cn',
            'Referer': 'https://login.189.cn/web/login',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'login_headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '127',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'login.189.cn',
            'Origin': 'https://login.189.cn',
            'Referer': 'https://login.189.cn/web/login',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        },
        'ecs_headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Host': 'www.189.cn',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        },
        'redirect_headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Host': 'www.189.cn',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        },
        'each_prov_headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Host': 'www.189.cn',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',

        },
        'user_headers': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Host': 'www.189.cn',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        }
    }
}


# #############################################################################
# ###################### 针对登录过程中用到的参数 ################################
# ############################################################################

# GET 请求

LOGIN_PARAMS = {
    '10086': {
        'send_flag': {
            'timestamp': '',  # 时间戳
        },
        'login': {
            'accountType': '01',
            'account': '',  # 手机号
            'password': '',  # 加密后的密码
            'pwdType': '01',
            'smsPwd': '',  # 短信验证码
            'inputCode': '',
            'backUrl': 'http://www.10086.cn/index/sc/index_280_280.html',   # 这里仅仅是针对四川
            'rememberMe': '0',
            'channelID': '12034',
            'loginMode': '01',
            'protocol': 'https:',
            'timestamp': '',  # 时间戳
        },
        'artifact': {
            'backUrl': 'http://www.10086.cn/index/sc/index_280_280.html',
            'artifact': '',  # artifact
            'type': '00'
        }
    },
    '10010': {
        'check_verify': {
            'callback': '',
            'userName': '',  # 手机号
            'pwdType': '02',
            '_': '',  # 时间戳
        },
        'send_mail': {
            'callback': '',
            'req_time': '',  # 时间戳
            'mobile': '',   # 手机号
            '_': '',    # 时间戳
        },
        'login': {
            'callback': '',
            'req_time': '',  # 时间戳
            'redirectURL': 'http://www.10010.com/net5/',
            'userName': '',  # 手机号
            'password': '',  # 短信验证码
            'pwdType': '02',
            'productType': '01',
            'redirectType': '01',
            'rememberMe': '1',
            '_': '',    # 时间戳
        },
        'check_release': {
            'callback': '',
            '_': '',    # 时间戳
        }
    },
    '189': {
        'captcha_params': {
            'undefined': '',
            'source': 'login',
            'width': '100',
            'height': '37'
        },
        'login_mail': {
            'm': 'sendphonepwd',
            'account': '',  # 手机号
            'uType': '201',
            'pid': '',  # 省份
            'captcha': '',  # 验证码
        }
    }
}

# POST请求

LOGIN_PAYLOADS = {
    '10086': {
        'check_number': {
            'userName': '',  # 手机号
            'loginMode': '01',
            'channelID': '10000'
        },
        'load_token': {
            'userName': '',  # 手机号
        },
        'send_code': {
            'userName': '',  # 手机号
            'type': '01',
            'channelID': '12034'
        }
    },
    '10010': {},        # 联通是个奇葩登录过程都是GET请求
    '189': {
        'check_payloads_1': {
            'm': 'checkphone',
            'phone': '',        # 手机号
        },
        'check_payloads_2': {
            'm': 'captcha',
            'account': '',      # 手机号
            'uType': '201',
            'ProvinceID': '',   # 省份id
            'areaCode': '',
            'cityNo': ''
        },
        'vaildate_payloads': {
            'uName': '',    # 手机号
            'uType': '201',
            'uPwd': '',     # 计算出的手机号
            'isRandomPwd': 'true',
        },
        'login_payloads': {
            'Account': '',  # 手机号
            'UType': '201',
            'ProvinceID': '',   # 省份
            'AreaCode': '',
            'CityNo': '',
            'Captcha': '',  # 验证码
            'RandomFlag': '1',
            'Password': '',     # 密码
        }
    }
}

