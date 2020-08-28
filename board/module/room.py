# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/26 21:24
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: room.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    :

"""

from ._pdbc import *


class Room(ModuleBase):
    key = PrimaryKeyField(primary_key=True)
    name = CharField(required=True)
    color = CharField(required=True)
    describe = CharField(required=True)
    capacity = IntegerField(required=True)
    available = BooleanField(required=True)

    create_time = DateTimeField(required=True)
