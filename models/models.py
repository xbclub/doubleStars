# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cangku(Base):
    __tablename__ = 'cangku'

    cangid = Column(INTEGER(11), primary_key=True)
    cangname = Column(String(20), nullable=False)


class Cate(Base):
    __tablename__ = 'cate'

    cid = Column(INTEGER(11), primary_key=True)
    cname = Column(String(20), nullable=False)


class User(Base):
    __tablename__ = 'user'

    uid = Column(INTEGER(11), primary_key=True)
    uname = Column(String(10), nullable=False)
    passwd = Column(String(32), nullable=False)
    nickname = Column(String(6), nullable=False)
    phone = Column(String(11), nullable=False)
    privilege = Column(INTEGER(1), nullable=False)


class Vip(Base):
    __tablename__ = 'vip'

    vid = Column(INTEGER(11), primary_key=True)
    vphone = Column(String(11), nullable=False)
    vname = Column(String(8), nullable=False)
    vrank = Column(String(255), nullable=False)


class Xiaoshou(Base):
    __tablename__ = 'xiaoshou'

    xid = Column(INTEGER(11), primary_key=True)
    uid = Column(INTEGER(11), nullable=False)
    pid = Column(INTEGER(11), nullable=False)
    value = Column(INTEGER(11), nullable=False)
    vid = Column(INTEGER(11))
    time = Column(Date, nullable=False)
    miaoshu = Column(Text, nullable=False)


class Product(Base):
    __tablename__ = 'product'

    pid = Column(INTEGER(11), primary_key=True)
    code = Column(String(32), nullable=False)
    name = Column(String(20), nullable=False)
    cid = Column(ForeignKey('cate.cid', ondelete='CASCADE'), nullable=False, index=True)
    caivalue = Column(String(11), nullable=False)
    shouvalue = Column(String(11), nullable=False)
    danwei = Column(INTEGER(1), nullable=False)
    color = Column(String(11), nullable=False)
    num = Column(String(255), nullable=False)

    cate = relationship('Cate')
