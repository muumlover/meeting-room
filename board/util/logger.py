#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/13 21:39
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: logger.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""

import logging

from aiologstash import create_tcp_handler


async def init_logger():
    handler = await create_tcp_handler('127.0.0.1', 5000)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(handler)
