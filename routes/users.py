from flask import Blueprint, render_template

# from config.connect import sql_query

users = Blueprint("users", __name__)


@users.route("/")
def userIndex():
    return render_template("index.html")


@users.route("/cate.html")
def userCates():
    return render_template("cate.html")


@users.route("/cangku.html")
def userCangku():
    return render_template("cangku.html")

@users.route("/vip.html")
def userVip():
    return render_template("vip.html")
