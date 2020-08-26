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
import json

from aiohttp import web

from module.room import Room
from util.response import Response


async def handle_query_rooms(request: web.Request):
    rooms = Room.objects()
    rooms_data = json.loads(rooms.to_json())
    return web.json_response({
        'rooms': rooms_data
    })


async def handle_add_rooms(request: web.Request):
    room_data = await request.json()
    if room_data.get('name', None) is None:
        raise web.HTTPBadRequest(text='key "name" is loss')
    room = Room(**room_data)
    rooms = Room.objects(name=room.name)
    if len(rooms) > 0:
        return web.json_response(Response.ROOM_EXIST)
    room.save()
    return web.json_response(Response.SUCCESS)
