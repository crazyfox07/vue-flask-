# -*- coding:utf-8 -*-
"""
File Name: vue_test
Version:
Description:
Author: liuxuewen
Date: 2018/7/12 14:23
"""
from flask import request
from flask_restful import Resource

from config.redis_config import get_proxies
from views import db
from orm.flask_orm import OcrOrm
import datetime

class HelloWorld(Resource):
    def get(self):
        page_no = request.args.get('pageNo')
        page_no = int(page_no)-1
        page_num = 10
        result = list()
        items = db.session.query(OcrOrm).limit(page_num).offset(page_no*page_num)
        for item in items:
            item_label_ali = item.label_ali
            item_label_tengxun = item.label_tengxun
            result.append({'date':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'name':item_label_ali,'address':item_label_tengxun})
        return {'result':result}

    def post(self):
        args = request.get_json()
        print(args)
        return {'hello': 'post'}


class GetProxy(Resource):
    def get(self):
        page_no = request.args.get('pageNo')
        page_no = int(page_no) - 1
        page_num = 10
        proxies = get_proxies(page_no,page_num)
        return {'result': proxies}