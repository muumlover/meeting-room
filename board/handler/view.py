#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/14 21:37
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: view.py
@Software: PyCharm 
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
import aiohttp_jinja2


async def handle_view(request):
    name = request.match_info.get('name', "Anonymous")

    context = {'name': name, 'surname': 'Svetlov'}
    response = aiohttp_jinja2.render_template('index.html', request, context)
    return response
