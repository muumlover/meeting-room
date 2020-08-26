#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/13 21:43
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: router.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""

from board.handler import *



def setup_router(router):
    router.add_route('GET', '/', handle_view)
    router.add_route('GET', '/echo', wshandle)
    router.add_route('GET', '/handle_query_rooms', handle_query_rooms)
    router.add_route('POST', '/handle_add_rooms', handle_add_rooms)
