#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/14 21:50
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: date_util.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
import calendar


def get_monthcalendar(year, month):
    return calendar.monthcalendar(year, month)


def get_monthrange(year, month):
    return calendar.monthrange(year, month)
