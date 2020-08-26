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


class Response:
    SUCCESS = {'code': 0, 'msg': '操作成功'}
    ROOM_EXIST = {'code': -1, 'msg': '已存在同名会议室'}
