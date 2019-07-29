from module import *
from models import *


class Cateinfo(object):
    def __init__(self, cid="", cname=""):
        self.cid = cid
        self.cname = cname

    def addCate(self):
        if self.cname == "":
            return return_json(-1, "分类名不能为空")
        try:
            db_session.add(Cate(cname=self.cname))
            db_session.commit()
            return return_json(1, "添加成功")
        except:
            db_session.rollback()
            return return_json(-1, "系统错误，添加失败")
        finally:
            db_session.remove()

    def listCate(self):
        if self.cname != "":
            rs = db_session.query(Cate).filter(Cate.cname.like('%' + self.cname + '%')).all()
        else:
            rs = db_session.query(Cate).all()
        jsons = []

        for i in rs:
            jsons.append({'cid': i.cid, 'cname': i.cname})
        return return_jsons(1, jsons)

    def editCate(self):
        if self.cid == "" or self.cname == "":
            return return_json(-1, "内容不全，请重新输入")
        try:
            rs = db_session.query(Cate).filter(Cate.cid == self.cid).first()
            rs.cname = self.cname
            db_session.commit()
            return return_json(1, "操作成功")
        except:
            db_session.rollback()
            return return_json(-1, "操作失败")
        finally:
            db_session.remove()

    def delCate(self):
        try:
            db_session.query(Cate).filter(Cate.cid == self.cid).delete()
            db_session.commit()
            return return_json(1, "删除成功")
        except:
            db_session.rollback()
            return return_json(-1, "删除失败")
        finally:
            db_session.remove()
