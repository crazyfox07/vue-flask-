# -*- coding:utf-8 -*-
"""
File Name: redis_config
Version:
Description:
Author: liuxuewen
Date: 2018/7/13 17:37
"""
import datetime
import redis
# redis
pool = redis.ConnectionPool(host='99.48.58.244', port=6379, db=13, password='mime@123')
# r = redis.Redis(connection_pool=pool)
r = redis.StrictRedis(connection_pool=pool)


def get_proxies(page_no, page_num):
    proxies = list()
    items = r.keys()
    items_len = len(items)
    start = page_no * page_num
    end = (page_no + 1) * page_num
    if start > items_len or end > items_len:
        items = items[items_len-page_num:items_len]
    else:
        items = items[start:end]
    for item in items:
        ip, port = item.decode(encoding='utf8').split(':')[-1].split('|')
        proxies.append({'ip':ip,'port':port,'date':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    return proxies


if __name__ == '__main__':
    get_proxies(1,10)