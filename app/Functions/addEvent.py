from app.Models.EventModel import Events
from app import db
from flask import Response, request
from datetime import datetime


def add_event():
    data = request.get_json()

    try:
        event_name = data["eventName"]
        date = data["date"]
    except KeyError:
        return Response("Invalid JSON Format", 422)

    try:
        formatted_date = datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
    except ValueError:
        return Response("Invalid Date Format", 422)

    if Events.query.filter(Events.eventName == event_name, Events.date == formatted_date).first():
        return Response("Event already exists", status=403)
    else:
        event = Events(eventName=event_name, date=formatted_date)
        db.session.add(event)
        db.session.commit()
        return Response("Successfully Added Event", status=200)
