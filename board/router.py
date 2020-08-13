#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/13 21:43
@Author  : Sam Wang
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: router.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wang. All rights reserved.
@Desc    : 
    
"""

from board.handler import *

router = web.UrlDispatcher()

router.add_route('GET', '/', handle)
router.add_route('GET', '/echo', wshandle)
router.add_route('GET', '/{name}', handle)
