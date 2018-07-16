# -*- coding:utf-8 -*-
"""
File Name: flask_orm
Version:
Description:
Author: liuxuewen
Date: 2018/7/13 9:59
"""
from views import db


class OcrOrm(db.Model):
    __tablename__ = 'tengxun_ocr'  # 定义表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_src = db.Column(db.Integer)
    label_ali = db.Column(db.String(256))
    label_tengxun = db.Column(db.String(256))
    img_b64 = db.Column(db.String(256))