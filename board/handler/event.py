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
            return web.json_response({
                'items': [to_json(event) for event in Event.objects()]
            })
        else:
            events = Event.objects(key=key)
            return web.json_response({
                'data': to_json(events[0]) if len(events) > 0 else None
            })

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
        event.describe = event_data.get('describe')
        event.date = datetime.strptime(event_data.get('date'), '%Y%m%d')
        event.start_time = datetime.strptime(event_data.get('start_time'), '%H:%M')
        event.end_time = datetime.strptime(event_data.get('end_time'), '%H:%M')
        event.create_time = datetime.now()

        event.room_key = room.key
        event.user_key = 0
        event.save()
        return web.json_response(Response.SUCCESS)
