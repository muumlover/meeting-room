# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/27 21:05
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: group.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
import json

from aiohttp import web

from module.group import Group


async def handle_query_groups(request: web.Request):
    return web.json_response({
        'items': [json.loads(room.to_json(use_db_field=False)) for room in Group.objects()]
    })
