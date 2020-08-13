#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/13 21:43
@Author  : Sam Wang
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: app.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wang. All rights reserved.
@Desc    : 
    
"""

from aiohttp import web

from board.router import router

app = web.Application(router=router)

if __name__ == '__main__':
    web.run_app(app)
