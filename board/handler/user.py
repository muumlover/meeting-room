# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/27 21:04
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: user.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
import json

from aiohttp import web

from module.user import User


async def handle_query_users(request: web.Request):
    return web.json_response({
        'items': [json.loads(room.to_json(use_db_field=False)) for room in User.objects()]
    })
