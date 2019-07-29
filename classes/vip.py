from module import *
from models import *
from flask import request, session


class Viper(object):
    def __init__(self, vphone="", vname="", vrank="0", vid=""):
        self.phone = vphone
        self.name = vname
        self.rank = vrank
        self.vid = vid

    def addVip(self):
        if self.name == "" or self.phone == "":
            return return_json(-1, "请填写完整信息")
        if len(self.phone) != 11:
            return return_json(-1, "手机号必须为11位数字")
        if not self.phone.isdigit():
            return return_json(-1, "手机号必须为纯数字")
        rs = db_session.query(Vip).filter(Vip.vphone == self.phone).count()
        if rs != 0:
            return return_json(-1, '用户已存在')
        try:
            db_session.add(Vip(vphone=self.phone, vname=self.name, vrank=self.rank))
            db_session.commit()
            return return_json(1, "添加成功")
        except:
            db_session.rollback()
            return return_json(-1, "添加失败")
        finally:
            db_session.remove()

    def editVip(self):
        if self.vid == "":
            return return_json(-1, "err")
        if self.name == "" or self.phone == "":
            return return_json(-1, "请填写完整信息")
        if len(self.phone) != 11:
            return return_json(-1, "手机号必须为11位数字")
        if not self.phone.isdigit():
            return return_json(-1, "手机号必须为纯数字")
        rs = db_session.query(Vip).filter(Vip.vid == self.vid).first()
        if rs.vphone !=self.phone:
            rs = db_session.query(Vip).filter(Vip.vphone == self.phone).count()
            if rs != 0:
                return return_json(-1, '用户已存在')
        try:
            rs = db_session.query(Vip).filter(Vip.vid == self.vid).first()
            rs.vphone = self.phone
            rs.vname = self.name
            db_session.commit()
            return return_json(1, "修改成功")
        except:
            db_session.rollback()
            return return_json(-1, "修改失败")
        finally:
            db_session.remove()

    def delVip(self):
        if self.vid == "":
            return return_json(-1, "err")
        try:
            db_session.query(Vip).filter(Vip.vid == self.vid).delete()
            db_session.commit()
            return return_json(1,"删除成功")
        except:
            db_session.rollback()
            return return_json(-1, "删除失败")
        finally:
            db_session.remove()

    def listVip(self):
        if self.phone != "":
            rs = db_session.query(Vip).filter(Vip.vphone.like('%' + self.phone + '%')).all()
        else:
            rs = db_session.query(Vip).all()
        jsons = []

        for i in rs:
            jsons.append({'vid': i.vid, 'vname': i.vname,'vphone':i.vphone,'vrank':i.vrank})
        return return_jsons(1, jsons)

    def checkVip(self):
        rs = db_session.query(Vip).filter(Vip.vphone == self.phone).count()
        if rs != 0:
            return return_json(-1, '用户已存在')
        else:
            return return_json(1,"手机号输入正确")