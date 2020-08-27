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


class RoomView(web.View):
    async def get(self):
        key = self.request.match_info.get('key', None)
        if not key:
            return web.json_response({
                'items': [json.loads(room.to_json(use_db_field=False)) for room in Room.objects()]
            })
        else:
            rooms = Room.objects(key=key)
            return web.json_response({
                'data': json.loads(rooms[0].to_json(use_db_field=False)) if len(rooms) > 0 else None
            })

    async def post(self):
        room_data = await self.request.json()
        if room_data.get('name', None) is None:
            raise web.HTTPBadRequest(text='key "name" is loss')
        room = Room(**room_data)
        rooms = Room.objects(name=room.name)
        if len(rooms) > 0:
            return web.json_response(Response.ROOM_EXIST)
        room.save()
        return web.json_response(Response.SUCCESS)
