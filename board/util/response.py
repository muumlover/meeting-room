# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/26 21:56
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: response.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
from aiohttp import web


class Response:
    SUCCESS = {'code': 0, 'msg': '操作成功'}
    UNKNOWN_ERROR = {'code': -1, 'msg': '未知错误'}
    ROOM_EXIST = {'code': -1, 'msg': '已存在同名会议室'}

    @staticmethod
    def list(func, objects):
        return web.json_response({
            'items': [func(room) for room in objects]
        })

    @staticmethod
    def data(func, objects):
        return web.json_response({
            'data': func(objects[0]) if len(objects) > 0 else None
        })
