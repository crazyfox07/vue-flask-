# -*- coding:utf-8 -*-
"""
File Name: __init__.py
Version:
Description:
Author: liuxuewen
Date: 2018/7/12 14:22
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.mysql_config import DevelopmentConfig
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app, supports_credentials=True)
db = SQLAlchemy(app) #实例化
