# TPHandler
移动,电信,联通等运营商的模拟登录以及查询详单(仅支持四川)

开发中，上传看心情........

- 11-20: 完成四川电信的登录模块
- 11-21: 完成四川电信的通话详单模块的开发并修改了登录模块的bug
- 11-26: 完成四川移动登录模块的开发
    - 移动很淘气啊，发验证短信时候，cookie没有按照升序排练，死活不给发，不过抖这个小机灵有意思么
- 11-27: 完成四川移动详情模块的发开,可以查询近半年的通话详单
- 12-04: 完成四川联通登录模块的开发
- 12-09: 研究了几天联通详单数据的采集，联通埋了毒，一直不能通过 checklogin验证
- 12-11: 在 /cu_test/ 目录下为我今天开发的联通调试已经信息提取测试，可行，再一次摸清楚了联通的脾气，调试过程完全复现了联通从登陆到请求数据所有的请求，也是为了获取关键的 security_verify_key ，实际上，这个值并不用。在实际过程中，不能缺的请求只有 获取验证码、登陆、验证、获取验证码、验证、获取数据 这个5次请求



## 声明
本人开发三大运营商的登录以及数据采集爬虫纯粹是技术好奇

近来不少大数据公司都栽在运营商的数据采集上，因此该项目开源仅仅作为交流学习用，商用以及非法用途作者我是很不建议的

反正我也仅仅是给一个demo而已，登录过程验证码的ocr也不会去涉及

笔者这里提供的是一个 登录+通话详单 的demo，别的功能可以自己去开发找寻乐趣