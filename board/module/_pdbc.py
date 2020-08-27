# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/26 21:24
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: _pdbc.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    :

"""
from bson import json_util

TYPE = 'MONGO'
if TYPE in ['SQLITE']:
    from peewee import SqliteDatabase

    from peewee import Model
    from peewee import CharField
    from peewee import IntegerField
    from peewee import BooleanField
    from peewee import DateField
    from peewee import TimeField
    from peewee import DateTimeField
    from peewee import PrimaryKeyField
    from peewee import TimestampField

    database = SqliteDatabase('meeting-room.db')
elif TYPE == 'MONGO':
    from mongoengine import connect

    from mongoengine import Document as ModuleBase
    from mongoengine import StringField as CharField
    from mongoengine import IntField as IntegerField
    from mongoengine import BooleanField
    from mongoengine import DateField
    from mongoengine import DateTimeField as TimeField
    from mongoengine import DateTimeField
    from mongoengine import SequenceField as PrimaryKeyField
    from mongoengine import IntField as TimestampField

    from mongoengine import ObjectIdField

    connect('meeting-room', host='mongodb://192.168.199.3/meeting-room')

if TYPE in ['SQLITE']:
    class ModuleBase(Model):
        class Meta:
            database = database

