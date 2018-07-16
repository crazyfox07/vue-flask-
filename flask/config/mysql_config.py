# -*- coding:utf-8 -*-
"""
File Name: mysql_config
Version:
Description:
Author: liuxuewen
Date: 2018/7/13 10:11
"""
class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACH_MODIFICATIONS = False

#开发环境
class DevelopmentConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'blog-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mime@123@99.48.58.95/spider?charset=utf8"
#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mime@123@99.48.58.95/spider?charset=utf8"

#生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI =  "mysql+pymysql://root:mime@123@99.48.58.95/spider?charset=utf8"