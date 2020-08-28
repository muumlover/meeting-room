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

    router.add_view(r'/api/room/{key:.*}', RoomView)
    router.add_view(r'/api/event/{key:.*}', EventView)

    router.add_route('GET', '/api/group', handle_query_groups)
    router.add_route('GET', '/api/user', handle_query_users)
