from module import *
from models import *


# from flask import request, session
class Cangkus(object):
    def __init__(self, cangkuid="", cangkuname=""):
        self.cid = cangkuid
        self.cname = cangkuname

    def addCangku(self):
        if self.cname == "":
            return return_json(-1, "货架名不能为空")
        try:
            db_session.add(Cangku(cangname=self.cname))
            db_session.commit()
            return return_json(1, "添加成功")
        except:
            db_session.rollback()
            return return_json(-1, "系统错误，添加失败")
        finally:
            db_session.remove()

    def listCangku(self):
        if self.cname != "":
            rs = db_session.query(Cangku).filter(Cangku.cangname.like('%' + self.cname + '%')).all()
        else:
            rs = db_session.query(Cangku).all()

        jsons = []

        for i in rs:
            jsons.append({'cid': i.cangid, 'cname': i.cangname})
        return return_jsons(1, jsons)

    def editCangku(self):
        if self.cid == "" or self.cname == "":
            return return_json(-1, "内容不全，请重新输入")
        try:
            rs = db_session.query(Cangku).filter(Cangku.cangid == self.cid).first()
            rs.cangname = self.cname
            db_session.commit()
            return return_json(1, "操作成功")
        except:
            db_session.rollback()
            return return_json(-1, "操作失败")
        finally:
            db_session.remove()

    def delCangku(self):
        try:
            db_session.query(Cangku).filter(Cangku.cangid == self.cid).delete()
            db_session.commit()
            return return_json(1, "删除成功")
        except:
            db_session.rollback()
            return return_json(-1, "删除失败")
        finally:
            db_session.remove()
