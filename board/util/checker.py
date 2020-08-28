# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/27 22:08
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: checker.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
from aiohttp import web
from mongoengine import ValidationError


class Checker:
    @staticmethod
    def cant_none(**kwargs):
        miss_field = []
        for k, v in kwargs.items():
            if v is None:
                miss_field.append(k)
            elif isinstance(v, ValidationError):
                miss_field.append(k)
            pass
        if miss_field:
            raise web.HTTPBadRequest(text=f'field {",".join(miss_field)} is required')
