# coding=utf-8

"""
    针对三大运营商所需要的js逆向
    此处为关键js 以及修改后的js
"""


# #########################
# ########## 电信 #########
# ########################


# 计算 trkId这个参数
TRKID_JS = """
    var trkid_js = function() {
        var CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.split('');
        var chars = CHARS, uuid = new Array(36), rnd=0, r;
        for (var i = 0; i < 36; i++) {
            if (i==8 || i==13 ||  i==18 || i==23) {
                uuid[i] = '-';
            } else if (i==14) {
                uuid[i] = '4';
            } else {
                if (rnd <= 0x02) rnd = 0x2000000 + (Math.random()*0x1000000)|0;
                r = rnd & 0xf;
                rnd = rnd >> 4;
                uuid[i] = chars[(i == 19) ? (r & 0x3) | 0x8 : r];
            }
        }
        return uuid.join('');
    };
"""

# code_v 似乎是个常量

CODE_V = '20170913'

# 计算lvid这个参数


LVID_JS = """
    var lvid = function(){
        var s=this;
        var a = '';
        if(!a){
            var b='abcdef1234567890'.split('');
            for(var n=0;n<32;n++){
                a+=b[Math.round(Math.random()*(b.length-1))]
                };
            var c=new Date;
            c.setTime(c.getTime()+5*365*24*60*60*1000);
            };
        return a;
    };
"""

# 计算s_fid这个参数

S_FID_JS = """
    var s_fid = function() {
        var c = "", b = "", d = "", f;
        f = 8;
        var e = 4;
        if (!c || 0 > c.indexOf("-")) {
            for (c = 0; 16 > c; c++)
                f = Math.floor(Math.random() * f),
                b += "0123456789ABCDEF".substring(f, f + 1),
                f = Math.floor(Math.random() * e),
                d += "0123456789ABCDEF".substring(f, f + 1),
                f = e = 16;
            c = b + "-" + d
        }
        return c
    };
"""

# nvid为常量

NVID = 1

# 目测 trkHmClickCoords 是个固定值，用来计算页面的
TRKHMCLICKCOORDS = '806%2C198%2C732'


# 计算 svid 来自访客验证环节
# 暂时未找到如何计算的

SVID_URL = 'https://webwebfenxi.189.cn:9002/b/ss/1/JS-1.5.1/s61709105264737'

SVID_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'webwebfenxi.189.cn:9002',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

SVID_PARAMS = {
    'AQB': '1',
    'rsid': 'eshipeship-189-all',
    'ndh': '1',
    'pf': '1',
    't': '8/9/2019 10:1:55 2 -480',
    'fid': '',  # s_fid
    'ce': 'UTF-8',
    'ns': 'eshipgdt',
    'pageName': '/web/login',
    'g': 'https://login.189.cn/web/login',
    'r': 'http://www.189.cn/html/login/index.html',
    'cc': 'CNY',
    'ch': '其它',
    'events': 'event99,event8',
    'c1': '/web/login',
    'v1': 'D=vid',
    'c2': 'D=g',
    'c3': '电信账号登录',
    'c4': 'login.189.cn',
    'c6': 'D=pid',
    'c7': 'D=oid',
    'c13': 'D=t',
    'c17': '',  # trkId
    'v17': '/web/login',
    'c18': '20190304',
    'c28': '1229',
    's': '1920x1080',
    'c': '24',
    'j': '1.6',
    'v': 'N',
    'k': 'Y',
    'bw': '801',
    'bh': '732',
    'AQE': '1'
}

# ECS_ReqInfo_login1 = ""
ECS_REQINFO_LOGIN1 = 'ECS_ReqInfo_login1'

# ASE 加密过程
ASE = """
var CryptoJS = CryptoJS || function(o, e) {
    var h = {}
      , g = h.lib = {}
      , z = function() {}
      , y = g.Base = {
        extend: function(b) {
            z.prototype = this;
            var d = new z;
            b && d.mixIn(b);
            d.hasOwnProperty("init") || (d.init = function() {
                d.$super.init.apply(this, arguments)
            }
            );
            d.init.prototype = d;
            d.$super = this;
            return d
        },
        create: function() {
            var b = this.extend();
            b.init.apply(b, arguments);
            return b
        },
        init: function() {},
        mixIn: function(b) {
            for (var d in b) {
                b.hasOwnProperty(d) && (this[d] = b[d])
            }
            b.hasOwnProperty("toString") && (this.toString = b.toString)
        },
        clone: function() {
            return this.init.prototype.extend(this)
        }
    }
      , a = g.WordArray = y.extend({
        init: function(b, d) {
            b = this.words = b || [];
            this.sigBytes = d != e ? d : 4 * b.length
        },
        toString: function(b) {
            return (b || m).stringify(this)
        },
        concat: function(b) {
            var p = this.words
              , n = b.words
              , l = this.sigBytes;
            b = b.sigBytes;
            this.clamp();
            if (l % 4) {
                for (var d = 0; d < b; d++) {
                    p[l + d >>> 2] |= (n[d >>> 2] >>> 24 - 8 * (d % 4) & 255) << 24 - 8 * ((l + d) % 4)
                }
            } else {
                if (65535 < n.length) {
                    for (d = 0; d < b; d += 4) {
                        p[l + d >>> 2] = n[d >>> 2]
                    }
                } else {
                    p.push.apply(p, n)
                }
            }
            this.sigBytes += b;
            return this
        },
        clamp: function() {
            var b = this.words
              , d = this.sigBytes;
            b[d >>> 2] &= 4294967295 << 32 - 8 * (d % 4);
            b.length = o.ceil(d / 4)
        },
        clone: function() {
            var b = y.clone.call(this);
            b.words = this.words.slice(0);
            return b
        },
        random: function(b) {
            for (var l = [], d = 0; d < b; d += 4) {
                l.push(4294967296 * o.random() | 0)
            }
            return new a.init(l,b)
        }
    })
      , k = h.enc = {}
      , m = k.Hex = {
        stringify: function(b) {
            var p = b.words;
            b = b.sigBytes;
            for (var n = [], l = 0; l < b; l++) {
                var d = p[l >>> 2] >>> 24 - 8 * (l % 4) & 255;
                n.push((d >>> 4).toString(16));
                n.push((d & 15).toString(16))
            }
            return n.join("")
        },
        parse: function(b) {
            for (var n = b.length, l = [], d = 0; d < n; d += 2) {
                l[d >>> 3] |= parseInt(b.substr(d, 2), 16) << 24 - 4 * (d % 8)
            }
            return new a.init(l,n / 2)
        }
    }
      , i = k.Latin1 = {
        stringify: function(b) {
            var n = b.words;
            b = b.sigBytes;
            for (var l = [], d = 0; d < b; d++) {
                l.push(String.fromCharCode(n[d >>> 2] >>> 24 - 8 * (d % 4) & 255))
            }
            return l.join("")
        },
        parse: function(b) {
            for (var n = b.length, l = [], d = 0; d < n; d++) {
                l[d >>> 2] |= (b.charCodeAt(d) & 255) << 24 - 8 * (d % 4)
            }
            return new a.init(l,n)
        }
    }
      , j = k.Utf8 = {
        stringify: function(b) {
            try {
                return decodeURIComponent(escape(i.stringify(b)))
            } catch (d) {
                throw Error("Malformed UTF-8 data")
            }
        },
        parse: function(b) {
            return i.parse(unescape(encodeURIComponent(b)))
        }
    }
      , c = g.BufferedBlockAlgorithm = y.extend({
        reset: function() {
            this._data = new a.init;
            this._nDataBytes = 0
        },
        _append: function(b) {
            "string" == typeof b && (b = j.parse(b));
            this._data.concat(b);
            this._nDataBytes += b.sigBytes
        },
        _process: function(l) {
            var t = this._data
              , s = t.words
              , p = t.sigBytes
              , n = this.blockSize
              , d = p / (4 * n)
              , d = l ? o.ceil(d) : o.max((d | 0) - this._minBufferSize, 0);
            l = d * n;
            p = o.min(4 * l, p);
            if (l) {
                for (var r = 0; r < l; r += n) {
                    this._doProcessBlock(s, r)
                }
                r = s.splice(0, l);
                t.sigBytes -= p
            }
            return new a.init(r,p)
        },
        clone: function() {
            var b = y.clone.call(this);
            b._data = this._data.clone();
            return b
        },
        _minBufferSize: 0
    });
    g.Hasher = c.extend({
        cfg: y.extend(),
        init: function(b) {
            this.cfg = this.cfg.extend(b);
            this.reset()
        },
        reset: function() {
            c.reset.call(this);
            this._doReset()
        },
        update: function(b) {
            this._append(b);
            this._process();
            return this
        },
        finalize: function(b) {
            b && this._append(b);
            return this._doFinalize()
        },
        blockSize: 16,
        _createHelper: function(b) {
            return function(d, l) {
                return (new b.init(l)).finalize(d)
            }
        },
        _createHmacHelper: function(b) {
            return function(d, l) {
                return (new f.HMAC.init(b,l)).finalize(d)
            }
        }
    });
    var f = h.algo = {};
    return h
}(Math);
(function() {
    var a = CryptoJS
      , b = a.lib.WordArray;
    a.enc.Base64 = {
        stringify: function(j) {
            var e = j.words
              , i = j.sigBytes
              , g = this._map;
            j.clamp();
            j = [];
            for (var h = 0; h < i; h += 3) {
                for (var c = (e[h >>> 2] >>> 24 - 8 * (h % 4) & 255) << 16 | (e[h + 1 >>> 2] >>> 24 - 8 * ((h + 1) % 4) & 255) << 8 | e[h + 2 >>> 2] >>> 24 - 8 * ((h + 2) % 4) & 255, f = 0; 4 > f && h + 0.75 * f < i; f++) {
                    j.push(g.charAt(c >>> 6 * (3 - f) & 63))
                }
            }
            if (e = g.charAt(64)) {
                for (; j.length % 4; ) {
                    j.push(e)
                }
            }
            return j.join("")
        },
        parse: function(k) {
            var f = k.length
              , i = this._map
              , h = i.charAt(64);
            h && (h = k.indexOf(h),
            -1 != h && (f = h));
            for (var h = [], j = 0, e = 0; e < f; e++) {
                if (e % 4) {
                    var g = i.indexOf(k.charAt(e - 1)) << 2 * (e % 4)
                      , c = i.indexOf(k.charAt(e)) >>> 6 - 2 * (e % 4);
                    h[j >>> 2] |= (g | c) << 24 - 8 * (j % 4);
                    j++
                }
            }
            return b.create(h, j)
        },
        _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    }
}
)();
(function(k) {
    function c(d, s, l, r, q, p, o) {
        d = d + (s & l | ~s & r) + q + o;
        return (d << p | d >>> 32 - p) + s
    }
    function f(d, s, l, r, q, p, o) {
        d = d + (s & r | l & ~r) + q + o;
        return (d << p | d >>> 32 - p) + s
    }
    function e(d, s, l, r, q, p, o) {
        d = d + (s ^ l ^ r) + q + o;
        return (d << p | d >>> 32 - p) + s
    }
    function n(d, s, l, r, q, p, o) {
        d = d + (l ^ (s | ~r)) + q + o;
        return (d << p | d >>> 32 - p) + s
    }
    for (var m = CryptoJS, a = m.lib, i = a.WordArray, j = a.Hasher, a = m.algo, g = [], h = 0; 64 > h; h++) {
        g[h] = 4294967296 * k.abs(k.sin(h + 1)) | 0
    }
    a = a.MD5 = j.extend({
        _doReset: function() {
            this._hash = new i.init([1732584193, 4023233417, 2562383102, 271733878])
        },
        _doProcessBlock: function(J, L) {
            for (var U = 0; 16 > U; U++) {
                var T = L + U
                  , S = J[T];
                J[T] = (S << 8 | S >>> 24) & 16711935 | (S << 24 | S >>> 8) & 4278255360
            }
            var U = this._hash.words
              , T = J[L + 0]
              , S = J[L + 1]
              , O = J[L + 2]
              , N = J[L + 3]
              , b = J[L + 4]
              , H = J[L + 5]
              , y = J[L + 6]
              , l = J[L + 7]
              , o = J[L + 8]
              , K = J[L + 9]
              , I = J[L + 10]
              , G = J[L + 11]
              , p = J[L + 12]
              , F = J[L + 13]
              , s = J[L + 14]
              , d = J[L + 15]
              , R = U[0]
              , M = U[1]
              , Q = U[2]
              , P = U[3]
              , R = c(R, M, Q, P, T, 7, g[0])
              , P = c(P, R, M, Q, S, 12, g[1])
              , Q = c(Q, P, R, M, O, 17, g[2])
              , M = c(M, Q, P, R, N, 22, g[3])
              , R = c(R, M, Q, P, b, 7, g[4])
              , P = c(P, R, M, Q, H, 12, g[5])
              , Q = c(Q, P, R, M, y, 17, g[6])
              , M = c(M, Q, P, R, l, 22, g[7])
              , R = c(R, M, Q, P, o, 7, g[8])
              , P = c(P, R, M, Q, K, 12, g[9])
              , Q = c(Q, P, R, M, I, 17, g[10])
              , M = c(M, Q, P, R, G, 22, g[11])
              , R = c(R, M, Q, P, p, 7, g[12])
              , P = c(P, R, M, Q, F, 12, g[13])
              , Q = c(Q, P, R, M, s, 17, g[14])
              , M = c(M, Q, P, R, d, 22, g[15])
              , R = f(R, M, Q, P, S, 5, g[16])
              , P = f(P, R, M, Q, y, 9, g[17])
              , Q = f(Q, P, R, M, G, 14, g[18])
              , M = f(M, Q, P, R, T, 20, g[19])
              , R = f(R, M, Q, P, H, 5, g[20])
              , P = f(P, R, M, Q, I, 9, g[21])
              , Q = f(Q, P, R, M, d, 14, g[22])
              , M = f(M, Q, P, R, b, 20, g[23])
              , R = f(R, M, Q, P, K, 5, g[24])
              , P = f(P, R, M, Q, s, 9, g[25])
              , Q = f(Q, P, R, M, N, 14, g[26])
              , M = f(M, Q, P, R, o, 20, g[27])
              , R = f(R, M, Q, P, F, 5, g[28])
              , P = f(P, R, M, Q, O, 9, g[29])
              , Q = f(Q, P, R, M, l, 14, g[30])
              , M = f(M, Q, P, R, p, 20, g[31])
              , R = e(R, M, Q, P, H, 4, g[32])
              , P = e(P, R, M, Q, o, 11, g[33])
              , Q = e(Q, P, R, M, G, 16, g[34])
              , M = e(M, Q, P, R, s, 23, g[35])
              , R = e(R, M, Q, P, S, 4, g[36])
              , P = e(P, R, M, Q, b, 11, g[37])
              , Q = e(Q, P, R, M, l, 16, g[38])
              , M = e(M, Q, P, R, I, 23, g[39])
              , R = e(R, M, Q, P, F, 4, g[40])
              , P = e(P, R, M, Q, T, 11, g[41])
              , Q = e(Q, P, R, M, N, 16, g[42])
              , M = e(M, Q, P, R, y, 23, g[43])
              , R = e(R, M, Q, P, K, 4, g[44])
              , P = e(P, R, M, Q, p, 11, g[45])
              , Q = e(Q, P, R, M, d, 16, g[46])
              , M = e(M, Q, P, R, O, 23, g[47])
              , R = n(R, M, Q, P, T, 6, g[48])
              , P = n(P, R, M, Q, l, 10, g[49])
              , Q = n(Q, P, R, M, s, 15, g[50])
              , M = n(M, Q, P, R, H, 21, g[51])
              , R = n(R, M, Q, P, p, 6, g[52])
              , P = n(P, R, M, Q, N, 10, g[53])
              , Q = n(Q, P, R, M, I, 15, g[54])
              , M = n(M, Q, P, R, S, 21, g[55])
              , R = n(R, M, Q, P, o, 6, g[56])
              , P = n(P, R, M, Q, d, 10, g[57])
              , Q = n(Q, P, R, M, y, 15, g[58])
              , M = n(M, Q, P, R, F, 21, g[59])
              , R = n(R, M, Q, P, b, 6, g[60])
              , P = n(P, R, M, Q, G, 10, g[61])
              , Q = n(Q, P, R, M, O, 15, g[62])
              , M = n(M, Q, P, R, K, 21, g[63]);
            U[0] = U[0] + R | 0;
            U[1] = U[1] + M | 0;
            U[2] = U[2] + Q | 0;
            U[3] = U[3] + P | 0
        },
        _doFinalize: function() {
            var d = this._data
              , q = d.words
              , l = 8 * this._nDataBytes
              , p = 8 * d.sigBytes;
            q[p >>> 5] |= 128 << 24 - p % 32;
            var o = k.floor(l / 4294967296);
            q[(p + 64 >>> 9 << 4) + 15] = (o << 8 | o >>> 24) & 16711935 | (o << 24 | o >>> 8) & 4278255360;
            q[(p + 64 >>> 9 << 4) + 14] = (l << 8 | l >>> 24) & 16711935 | (l << 24 | l >>> 8) & 4278255360;
            d.sigBytes = 4 * (q.length + 1);
            this._process();
            d = this._hash;
            q = d.words;
            for (l = 0; 4 > l; l++) {
                p = q[l],
                q[l] = (p << 8 | p >>> 24) & 16711935 | (p << 24 | p >>> 8) & 4278255360
            }
            return d
        },
        clone: function() {
            var d = j.clone.call(this);
            d._hash = this._hash.clone();
            return d
        }
    });
    m.MD5 = j._createHelper(a);
    m.HmacMD5 = j._createHmacHelper(a)
}
)(Math);
(function() {
    var b = CryptoJS
      , e = b.lib
      , f = e.Base
      , a = e.WordArray
      , e = b.algo
      , c = e.EvpKDF = f.extend({
        cfg: f.extend({
            keySize: 4,
            hasher: e.MD5,
            iterations: 1
        }),
        init: function(g) {
            this.cfg = this.cfg.extend(g)
        },
        compute: function(k, g) {
            for (var i = this.cfg, t = i.hasher.create(), l = a.create(), o = l.words, h = i.keySize, i = i.iterations; o.length < h; ) {
                j && t.update(j);
                var j = t.update(k).finalize(g);
                t.reset();
                for (var m = 1; m < i; m++) {
                    j = t.finalize(j),
                    t.reset()
                }
                l.concat(j)
            }
            l.sigBytes = 4 * h;
            return l
        }
    });
    b.EvpKDF = function(i, g, h) {
        return c.create(h).compute(i, g)
    }
}
)();
CryptoJS.lib.Cipher || function(B) {
    var g = CryptoJS
      , j = g.lib
      , i = j.Base
      , D = j.WordArray
      , C = j.BufferedBlockAlgorithm
      , e = g.enc.Base64
      , z = g.algo.EvpKDF
      , A = j.Cipher = C.extend({
        cfg: i.extend(),
        createEncryptor: function(c, b) {
            return this.create(this._ENC_XFORM_MODE, c, b)
        },
        createDecryptor: function(c, b) {
            return this.create(this._DEC_XFORM_MODE, c, b)
        },
        init: function(l, d, c) {
            this.cfg = this.cfg.extend(c);
            this._xformMode = l;
            this._key = d;
            this.reset()
        },
        reset: function() {
            C.reset.call(this);
            this._doReset()
        },
        process: function(a) {
            this._append(a);
            return this._process()
        },
        finalize: function(a) {
            a && this._append(a);
            return this._doFinalize()
        },
        keySize: 4,
        ivSize: 4,
        _ENC_XFORM_MODE: 1,
        _DEC_XFORM_MODE: 2,
        _createHelper: function(a) {
            return {
                encrypt: function(c, l, n) {
                    return ("string" == typeof l ? k : o).encrypt(a, c, l, n)
                },
                decrypt: function(c, l, n) {
                    return ("string" == typeof l ? k : o).decrypt(a, c, l, n)
                }
            }
        }
    });
    j.StreamCipher = A.extend({
        _doFinalize: function() {
            return this._process(!0)
        },
        blockSize: 1
    });
    var m = g.mode = {}
      , y = function(p, n, l) {
        var r = this._iv;
        r ? this._iv = B : r = this._prevBlock;
        for (var q = 0; q < l; q++) {
            p[n + q] ^= r[q]
        }
    }
      , f = (j.BlockCipherMode = i.extend({
        createEncryptor: function(c, b) {
            return this.Encryptor.create(c, b)
        },
        createDecryptor: function(c, b) {
            return this.Decryptor.create(c, b)
        },
        init: function(c, b) {
            this._cipher = c;
            this._iv = b
        }
    })).extend();
    f.Encryptor = f.extend({
        processBlock: function(n, l) {
            var d = this._cipher
              , p = d.blockSize;
            y.call(this, n, l, p);
            d.encryptBlock(n, l);
            this._prevBlock = n.slice(l, l + p)
        }
    });
    f.Decryptor = f.extend({
        processBlock: function(p, n) {
            var l = this._cipher
              , r = l.blockSize
              , q = p.slice(n, n + r);
            l.decryptBlock(p, n);
            y.call(this, p, n, r);
            this._prevBlock = q
        }
    });
    m = m.CBC = f;
    f = (g.pad = {}).Pkcs7 = {
        pad: function(r, p) {
            for (var u = 4 * p, u = u - r.sigBytes % u, s = u << 24 | u << 16 | u << 8 | u, q = [], t = 0; t < u; t += 4) {
                q.push(s)
            }
            u = D.create(q, u);
            r.concat(u)
        },
        unpad: function(b) {
            b.sigBytes -= b.words[b.sigBytes - 1 >>> 2] & 255
        }
    };
    j.BlockCipher = A.extend({
        cfg: A.cfg.extend({
            mode: m,
            padding: f
        }),
        reset: function() {
            A.reset.call(this);
            var l = this.cfg
              , d = l.iv
              , l = l.mode;
            if (this._xformMode == this._ENC_XFORM_MODE) {
                var n = l.createEncryptor
            } else {
                n = l.createDecryptor,
                this._minBufferSize = 1
            }
            this._mode = n.call(l, this, d && d.words)
        },
        _doProcessBlock: function(d, c) {
            this._mode.processBlock(d, c)
        },
        _doFinalize: function() {
            var d = this.cfg.padding;
            if (this._xformMode == this._ENC_XFORM_MODE) {
                d.pad(this._data, this.blockSize);
                var c = this._process(!0)
            } else {
                c = this._process(!0),
                d.unpad(c)
            }
            return c
        },
        blockSize: 4
    });
    var h = j.CipherParams = i.extend({
        init: function(b) {
            this.mixIn(b)
        },
        toString: function(b) {
            return (b || this.formatter).stringify(this)
        }
    })
      , m = (g.format = {}).OpenSSL = {
        stringify: function(d) {
            var c = d.ciphertext;
            d = d.salt;
            return (d ? D.create([1398893684, 1701076831]).concat(d).concat(c) : c).toString(e)
        },
        parse: function(l) {
            l = e.parse(l);
            var d = l.words;
            if (1398893684 == d[0] && 1701076831 == d[1]) {
                var n = D.create(d.slice(2, 4));
                d.splice(0, 4);
                l.sigBytes -= 16
            }
            return h.create({
                ciphertext: l,
                salt: n
            })
        }
    }
      , o = j.SerializableCipher = i.extend({
        cfg: i.extend({
            format: m
        }),
        encrypt: function(q, n, s, r) {
            r = this.cfg.extend(r);
            var p = q.createEncryptor(s, r);
            n = p.finalize(n);
            p = p.cfg;
            return h.create({
                ciphertext: n,
                key: s,
                iv: p.iv,
                algorithm: q,
                mode: p.mode,
                padding: p.padding,
                blockSize: q.blockSize,
                formatter: r.format
            })
        },
        decrypt: function(n, l, q, p) {
            p = this.cfg.extend(p);
            l = this._parse(l, p.format);
            return n.createDecryptor(q, p).finalize(l.ciphertext)
        },
        _parse: function(d, c) {
            return "string" == typeof d ? c.parse(d, this) : d
        }
    })
      , g = (g.kdf = {}).OpenSSL = {
        execute: function(n, l, q, p) {
            p || (p = D.random(8));
            n = z.create({
                keySize: l + q
            }).compute(n, p);
            q = D.create(n.words.slice(l), 4 * q);
            n.sigBytes = 4 * l;
            return h.create({
                key: n,
                iv: q,
                salt: p
            })
        }
    }
      , k = j.PasswordBasedCipher = o.extend({
        cfg: o.cfg.extend({
            kdf: g
        }),
        encrypt: function(a, q, p, n) {
            n = this.cfg.extend(n);
            p = n.kdf.execute(p, a.keySize, a.ivSize);
            n.iv = p.iv;
            a = o.encrypt.call(this, a, q, p.key, n);
            a.mixIn(p);
            return a
        },
        decrypt: function(a, q, p, n) {
            n = this.cfg.extend(n);
            q = this._parse(q, n.format);
            p = n.kdf.execute(p, a.keySize, a.ivSize, q.salt);
            n.iv = p.iv;
            return o.decrypt.call(this, a, q, p.key, n)
        }
    })
}();
(function() {
    for (var C = CryptoJS, K = C.lib.BlockCipher, Q = C.algo, M = [], E = [], D = [], I = [], m = [], A = [], S = [], h = [], J = [], L = [], T = [], R = 0; 256 > R; R++) {
        T[R] = 128 > R ? R << 1 : R << 1 ^ 283
    }
    for (var P = 0, O = 0, R = 0; 256 > R; R++) {
        var N = O ^ O << 1 ^ O << 2 ^ O << 3 ^ O << 4
          , N = N >>> 8 ^ N & 255 ^ 99;
        M[P] = N;
        E[N] = P;
        var f = T[P]
          , B = T[f]
          , o = T[B]
          , g = 257 * T[N] ^ 16843008 * N;
        D[P] = g << 24 | g >>> 8;
        I[P] = g << 16 | g >>> 16;
        m[P] = g << 8 | g >>> 24;
        A[P] = g;
        g = 16843009 * o ^ 65537 * B ^ 257 * f ^ 16843008 * P;
        S[N] = g << 24 | g >>> 8;
        h[N] = g << 16 | g >>> 16;
        J[N] = g << 8 | g >>> 24;
        L[N] = g;
        P ? (P = f ^ T[T[T[o ^ f]]],
        O ^= T[T[O]]) : P = O = 1
    }
    var i = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
      , Q = Q.AES = K.extend({
        _doReset: function() {
            for (var b = this._key, r = b.words, q = b.sigBytes / 4, b = 4 * ((this._nRounds = q + 6) + 1), p = this._keySchedule = [], n = 0; n < b; n++) {
                if (n < q) {
                    p[n] = r[n]
                } else {
                    var l = p[n - 1];
                    n % q ? 6 < q && 4 == n % q && (l = M[l >>> 24] << 24 | M[l >>> 16 & 255] << 16 | M[l >>> 8 & 255] << 8 | M[l & 255]) : (l = l << 8 | l >>> 24,
                    l = M[l >>> 24] << 24 | M[l >>> 16 & 255] << 16 | M[l >>> 8 & 255] << 8 | M[l & 255],
                    l ^= i[n / q | 0] << 24);
                    p[n] = p[n - q] ^ l
                }
            }
            r = this._invKeySchedule = [];
            for (q = 0; q < b; q++) {
                n = b - q,
                l = q % 4 ? p[n] : p[n - 4],
                r[q] = 4 > q || 4 >= n ? l : S[M[l >>> 24]] ^ h[M[l >>> 16 & 255]] ^ J[M[l >>> 8 & 255]] ^ L[M[l & 255]]
            }
        },
        encryptBlock: function(d, c) {
            this._doCryptBlock(d, c, this._keySchedule, D, I, m, A, M)
        },
        decryptBlock: function(b, j) {
            var e = b[j + 1];
            b[j + 1] = b[j + 3];
            b[j + 3] = e;
            this._doCryptBlock(b, j, this._invKeySchedule, S, h, J, L, E);
            e = b[j + 1];
            b[j + 1] = b[j + 3];
            b[j + 3] = e
        },
        _doCryptBlock: function(ac, ab, aa, Z, Y, U, G, X) {
            for (var F = this._nRounds, W = ac[ab] ^ aa[0], V = ac[ab + 1] ^ aa[1], H = ac[ab + 2] ^ aa[2], z = ac[ab + 3] ^ aa[3], y = 4, w = 1; w < F; w++) {
                var x = Z[W >>> 24] ^ Y[V >>> 16 & 255] ^ U[H >>> 8 & 255] ^ G[z & 255] ^ aa[y++]
                  , v = Z[V >>> 24] ^ Y[H >>> 16 & 255] ^ U[z >>> 8 & 255] ^ G[W & 255] ^ aa[y++]
                  , u = Z[H >>> 24] ^ Y[z >>> 16 & 255] ^ U[W >>> 8 & 255] ^ G[V & 255] ^ aa[y++]
                  , z = Z[z >>> 24] ^ Y[W >>> 16 & 255] ^ U[V >>> 8 & 255] ^ G[H & 255] ^ aa[y++]
                  , W = x
                  , V = v
                  , H = u
            }
            x = (X[W >>> 24] << 24 | X[V >>> 16 & 255] << 16 | X[H >>> 8 & 255] << 8 | X[z & 255]) ^ aa[y++];
            v = (X[V >>> 24] << 24 | X[H >>> 16 & 255] << 16 | X[z >>> 8 & 255] << 8 | X[W & 255]) ^ aa[y++];
            u = (X[H >>> 24] << 24 | X[z >>> 16 & 255] << 16 | X[W >>> 8 & 255] << 8 | X[V & 255]) ^ aa[y++];
            z = (X[z >>> 24] << 24 | X[W >>> 16 & 255] << 16 | X[V >>> 8 & 255] << 8 | X[H & 255]) ^ aa[y++];
            ac[ab] = x;
            ac[ab + 1] = v;
            ac[ab + 2] = u;
            ac[ab + 3] = z
        },
        keySize: 8
    });
    C.AES = K._createHelper(Q)
}
)();

var ase = function(e) {
    var a = CryptoJS.MD5("login.189.cn");
    var c = CryptoJS.enc.Utf8.parse(a);
    var b = CryptoJS.enc.Utf8.parse("1234567812345678");
    var d = CryptoJS.AES.encrypt(e, c, {
        iv: b
    });
    return d + ""
}
;

function login1(e) {
    var a = "ECS_ReqInfo_login1";
    var c = "";
    var b = "login.189.cn";
    c = e;
    c = CryptoJS.AES.encrypt(c, b);
    d = cookie_d(a, c, {expires: 30,path: "/"})
    return d;
}

var cookie_d  = function(q, p, v) {return h(p)};
function h(i) {return d(String(i));}
function d(i) {return encodeURIComponent(i);}

"""

# #########################
# ########## 联通 #########
# ########################


DCSFPC = """
    function dcsFPC() {
        var WT = {};
        var name = 'WT_FPC';
        var dCur = new Date();
        var adj = 0;
        var dExp = new Date(dCur.getTime() + 315360000000);
        var dSes = new Date(dCur.getTime());
        WT.co_f = WT.vt_sid = WT.vt_f = WT.vt_f_a = WT.vt_f_s = WT.vt_f_d = WT.vt_f_tlh = WT.vt_f_tlv = "";
        WT.co_f="2";
        var cur=dCur.getTime().toString();
        for (var i=2;i<=(32-cur.length);i++){
            WT.co_f+=Math.floor(Math.random()*16.0).toString(16);
            }
        WT.co_f+=cur;
        WT.vt_f="1";
        WT.vt_f_a="1";
        WT.vt_f_s=WT.vt_f_d="1";
        WT.vt_f_tlh=WT.vt_f_tlv="0";
        WT.co_f = escape(WT.co_f);
        WT.vt_sid = WT.co_f + "." + (dSes.getTime() - adj);
        var expiry = "; expires=" + dExp.toGMTString();
        //return name + "=" + "id=" + WT.co_f + ";lv=" + dCur.getTime().toString() + ";ss=" + dSes.getTime().toString();
        return { 'WT_FPC': "id=" + WT.co_f, 'lv': dCur.getTime().toString(), 'ss': dSes.getTime().toString()}
    }
"""

N3FA_CID = """
     function uuid() {
            var d = new Date().getTime();
            var uuid = 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
                var r = (d + Math.random() * 16) % 16 | 0;
                d = Math.floor(d / 16);
                return (c == 'x' ? r : (r & 0x7 | 0x8)).toString(16);
            });
            return uuid;
        };
"""

N3FA_EXT = """
    var extToServerParamNames = "ft".split(" ");
    function buildExt() {
        var _ext = {};
        _ext.ft = nowTimeOnSecond();
        return generateStringWithObjProperty(_ext, extToServerParamNames, "^");
    };
    function nowTimeOnSecond() {
        return Math.round(new Date().getTime() / 1E3);
    };
    function generateStringWithObjProperty(obj, propertys, join) {
        for (var valuesToSend = [], i = 0, length = propertys.length; i < length; i++) {
            var propertyName = propertys[i], propertyValue = obj[propertyName];
            "undefined" != typeof propertyValue && "" !== propertyValue
            && valuesToSend.push(propertyName + "=" + encodeURIComponent(propertyValue))
        }
        return valuesToSend.join(join)
    }; 
"""

N3FA_ID = 'a9e72dfe4a54a20c3d6e671b3bad01d9'

N3FA_LVT = ''.join(['_n3fa_lvt', N3FA_ID])

N3FA_LPVT = ''.join(['_n3fa_lpvt', N3FA_ID])

# #########################
# ########## 移动 #########
# ########################


COLLECT_ID = """
    var cid = function(){
        var lc_ci = "";
        while (lc_ci.length < 32) {
            lc_ci += Math.random().toString(35).substr(2, 32);
        }
        lc_ci = lc_ci.substr(0,32);
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + 73000);
        return lc_ci;
    }
"""

WTFPC = """
    function wtfpc() {
        var WT = {};
        var name = 'WT_FPC';
        var dCur = new Date();
        var adj = 0;
        var dExp = new Date(dCur.getTime() + 315360000000);
        var dSes = new Date(dCur.getTime());
        WT.co_f = WT.vt_sid = WT.vt_f = WT.vt_f_a = WT.vt_f_s = WT.vt_f_d = WT.vt_f_tlh = WT.vt_f_tlv = "";
        WT.co_f="2";
        var cur=dCur.getTime().toString();
        for (var i=2;i<=(32-cur.length);i++){
            WT.co_f+=Math.floor(Math.random()*16.0).toString(16);
            }
        WT.co_f+=cur;
        WT.vt_f="1";
        WT.vt_f_a="1";
        WT.vt_f_s=WT.vt_f_d="1";
        WT.vt_f_tlh=WT.vt_f_tlv="0";
        WT.co_f = escape(WT.co_f);
        WT.vt_sid = WT.co_f + "." + (dSes.getTime() - adj);
        var expiry = "; expires=" + dExp.toGMTString();
        return "id=" + WT.co_f + ":lv=" + dCur.getTime().toString() + ":ss=" + dSes.getTime().toString();
    }
"""