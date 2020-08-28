# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/26 21:24
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: event.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    :

"""
from ._pdbc import *


class Event(ModuleBase):
    key = PrimaryKeyField(primary_key=True)
    name = CharField(required=True)
    describe = CharField(required=True)
    date = DateField(required=True)
    start_time = TimeField(required=True)
    end_time = TimeField(required=True)

    room_key = IntegerField(required=True)
    user_key = IntegerField(required=True)

    create_time = DateTimeField(required=True)
