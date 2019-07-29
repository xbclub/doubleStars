from module import *
from models import *
from flask import request, session


class Login(object):
    def __init__(self):
        self.username = request.form['username']
        self.password = request.form['password']
        try:
            self.nickname = request.form['nickname']
            self.phone = request.form['phone']
            self.privilege = int(request.form['privilege'])
        except KeyError:
            self.nickname = ""
            self.phone = ""
            self.privilege = None

    def reg(self):
        try:
            session['privilege'] != "1"
            return return_json(-1, "无权操作")
        except KeyError:
            return return_json(-1, "请先登录")

        if self.username == "" or self.password == "" or self.nickname == "" or self.privilege == "":
            return return_json(-1, "数据输入不完整")
        if len(self.phone) != 11:
            return return_json(-1, "手机号不合法")
        if self.privilege < 0 or self.privilege > 1:
            return return_json(-1, "用户权限不合法")
        try:
            db_session.add(
                User(uname=self.username, passwd=pwd(self.password), nickname=self.nickname, phone=self.phone,
                     privilege=self.privilege))
            db_session.commit()
            return return_json(1, "注册成功")
        except:
            db_session.rollback()
            return return_json(-1, "服务器错误")
        finally:
            db_session.remove()

    def loginit(self):
        if self.username == "" or self.password == "":
            return return_json(-1, "用户名和密码不能为空！")
        try:
            rs = db_session.query(User).filter(User.uname == self.username).first()
            if rs.passwd == pwd(self.password):
                session['uid'] = rs.uid
                session['username'] = rs.uname
                session['nickname'] = rs.nickname
                session['privilege'] = rs.privilege
                return return_json(1, "登陆成功")
            else:
                return return_json(-1, "用户名或密码错误")
        except:
            db_session.rollback()
            return return_json(-1, "用户名或密码错误")
        finally:
            db_session.remove()

    def userquery(self):
        rs = db_session.query(User).all()
        jsons = []
        for i in rs:
            jsons.append({"uid": rs.uid, "uname": rs.uname, "nickname": rs.nickname, "phone": rs.phone,
                          "privilege": rs.privilege})
        return return_jsons(1, jsons)
