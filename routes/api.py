from flask import Blueprint, request
from classes import *
from module import *

api = Blueprint("api", __name__)


@api.route("/reg", methods=['POST'])
def reg():
    login = Login()
    return login.reg()


@api.route("/login", methods=['POST'])
def loginit():
    login = Login()
    return login.loginit()


@api.route("/userlist", methods=['POST'])
def userlist():
    login = Login()
    return login.userquery()


@api.route("/cateadd", methods=['POST'])
def cateadd():
    try:
        cname = request.form['cname']
    except:
        return return_json(-1, "参数错误")
    cate = Cateinfo(cname=cname)
    return cate.addCate()


@api.route("/catelist")
def catelist():
    cate = Cateinfo()
    return cate.listCate()


@api.route("/catequery", methods=['POST'])
def catequery():
    try:
        cname = request.form['cname']
    except:
        cname = ""
    cate = Cateinfo(cname=cname)
    return cate.listCate()


@api.route("/cateedit", methods=['POST'])
def cateedit():
    try:
        cname = request.form['cname']
        cid = request.form['cid']
    except:
        cname = ""
        cid = ""
    cate = Cateinfo(cid, cname)
    return cate.editCate()


@api.route("/catedel", methods=['POST'])
def catedel():
    try:
        cid = request.form['cid']
    except:
        return return_json(-1,"id不合法")
    cate = Cateinfo(cid)
    return cate.delCate()


@api.route("/cangkulist")
def cangkulist():
    cangku = Cangkus()
    return cangku.listCangku()


@api.route("/cangkuadd", methods=['POST'])
def cangkuadd():
    try:
        cname = request.form['cname']
    except:
        return return_json(-1, "参数错误")
    cate = Cangkus(cangkuname=cname)
    return cate.addCangku()


@api.route("/cangkudel", methods=['POST'])
def cangkudel():
    try:
        cid = request.form['cid']
    except:
        return return_json(-1,"id不合法")
    cangku = Cangkus(cid)
    return cangku.delCangku()


@api.route("/cangkuedit", methods=['POST'])
def cangkuedit():
    try:
        cname = request.form['cname']
        cid = request.form['cid']
    except:
        cname = ""
        cid = ""
    cangku = Cangkus(cid, cname)
    return cangku.editCangku()


@api.route("/cangkuquery", methods=['POST'])
def cangkuquery():
    try:
        cname = request.form['cname']
    except:
        cname = ""
    cangku = Cangkus(cangkuname=cname)
    return cangku.listCangku()


@api.route("/vipadd", methods=['POST'])
def vipadd():
    try:
        vname = request.form['vname']
        vphone = request.form['vphone']
    except:
        return return_json(-1, "参数错误")
    vip = Viper(vphone=vphone, vname=vname)
    return vip.addVip()

@api.route("/vipcheck", methods=['POST'])
def vipcheck():
    try:
        vphone = request.form['vphone']
    except:
        return return_json(-1, "参数错误")
    if len(vphone) != 11:
        return return_json(-1,"手机号必须为11位数字")
    if not vphone.isdigit():
        return return_json(-1,"手机号必须为纯数字")
    vip = Viper(vphone=vphone)
    return vip.checkVip()

@api.route("/viplist")
def viplist():
    vip = Viper()
    return vip.listVip()

@api.route("/vipedit",methods=['POST'])
def vipedit():
    try:
        vid=request.form['vid']
        vname = request.form['vname']
        vphone = request.form['vphone']
    except:
        return return_json(-1, "参数错误")
    vip = Viper(vphone=vphone, vname=vname,vid=vid)
    return vip.editVip()

@api.route("/vipdel", methods=['POST'])
def vipdel():
    try:
        vid = request.form['vid']
    except:
        return return_json(-1,"id不合法")
    vip = Viper(vid=vid)
    return vip.delVip()

@api.route("/vipquery", methods=['POST'])
def vipquery():
    try:
        vphone = request.form['vphone']
    except:
        vphone = ""
    vip = Viper(vphone=vphone)
    return vip.listVip()