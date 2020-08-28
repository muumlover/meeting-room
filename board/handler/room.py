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
from datetime import datetime

from aiohttp import web
from mongoengine import ValidationError

from module.room import Room
from util.checker import Checker
from util.response import Response


class RoomView(web.View):
    async def get(self):
        key = self.request.match_info.get('key', None)

        def to_json(room):
            return {
                'key': room.key,
                'name': room.name,
                'color': room.color,
                'describe': room.describe,
                'capacity': room.capacity
            }

        if not key:
            return Response.list(to_json, Room.objects())
        else:
            return Response.data(to_json, Room.objects(key=key))

    async def post(self):
        room_data = await self.request.json()

        room_name = room_data.get('name')
        Checker.cant_none(room_name=room_name)
        rooms = Room.objects(name=room_name)
        if len(rooms) > 0:
            return web.json_response(Response.ROOM_EXIST)

        room = Room(**room_data)
        room.name = room_data.get('name')
        room.color = room_data.get('color')
        room.describe = room_data.get('describe', '无')
        room.capacity = room_data.get('capacity', 0)
        room.available = room_data.get('available', True)

        room.create_time = datetime.now()

        try:
            room.save()
        except ValidationError as e:
            Checker.cant_none(**e.errors)
        return web.json_response(Response.SUCCESS)
