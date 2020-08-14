#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/13 21:43
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: app.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
import logging
import pathlib

import aiohttp_jinja2
import jinja2
from aiohttp import web

from board.router import setup_router

app = web.Application()

base_path = pathlib.Path.cwd() / 'board'
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(base_path / 'template')))
# app.router.add_static('/static', base_path / 'static')

setup_router(app.router)

if __name__ == '__main__':
    logging.basicConfig(
        format='%(levelname)s: %(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
        level=logging.NOTSET
    )
    web.run_app(app)
