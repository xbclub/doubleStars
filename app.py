# from routes.admin import admin
# from routes.api import api
# from routes.users import users
from flask import Flask,blueprints
from routes import *
from datetime import timedelta
import os

app = Flask(__name__)
app.env = "production"
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=3)
app.register_blueprint(index, url_prefix='/')
# app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(users, url_prefix='/users')
# 修改jinja2的调用变为{[ ]}
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'


# @app.errorhandler(405)
# def not_found(error):
#     print(error)
#     return "小伙子不要总想着搞事", 404


if __name__ == '__main__':
    app.run(host="0.0.0.0")