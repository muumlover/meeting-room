# !/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/8/27 21:05
@Author  : Sam Wong
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : MeetingRoom
@FileName: event.py
@Software: PyCharm
@license : (C) Copyright 2020 by Sam Wong. All rights reserved.
@Desc    : 
    
"""
from datetime import datetime

from aiohttp import web
from mongoengine import ValidationError

from module.event import Event
from module.room import Room
from util.checker import Checker
from util.response import Response


class EventView(web.View):
    async def get(self):
        key = self.request.match_info.get('key', None)

        def to_json(event):
            return {
                'key': event.key,
                'name': event.name,
                'describe': event.describe,
                'date': event.date.strftime('%Y%m%d'),
                'start_time': event.start_time.strftime('%H:%M'),
                'end_time': event.end_time.strftime('%H:%M')
            }

        if not key:
            return Response.list(to_json, Event.objects())
        else:
            return Response.data(to_json, Event.objects(key=key))

    async def post(self):
        event_data = await self.request.json()

        room_key = event_data.get('room_key')
        Checker.cant_none(room_key=room_key)
        rooms = Room.objects(key=room_key)
        if not rooms:
            return web.json_response(Response.UNKNOWN_ERROR)
        room = rooms[0]

        event = Event()
        event.name = event_data.get('name')
        event.describe = event_data.get('describe', '无')
        event.date = datetime.strptime(event_data.get('date'), '%Y%m%d')
        event.start_time = datetime.strptime(event_data.get('start_time'), '%H:%M')
        event.end_time = datetime.strptime(event_data.get('end_time'), '%H:%M')

        event.room_key = room.key
        event.user_key = 0

        event.create_time = datetime.now()

        try:
            event.save()
        except ValidationError as e:
            Checker.cant_none(**e.errors)
        return web.json_response(Response.SUCCESS)
