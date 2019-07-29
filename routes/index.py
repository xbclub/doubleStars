from flask import Blueprint, render_template

# from config.connect import sql_query

index = Blueprint("index", __name__)


@index.route("/")
def indexs():
    #
    # sql="select * from user"
    # data=sql_query(sql,())
    return render_template("login.html")


@index.route("/test", methods=['POST'])
def test():
    return "helloworld!"
