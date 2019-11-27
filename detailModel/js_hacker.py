# coding=utf-8

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