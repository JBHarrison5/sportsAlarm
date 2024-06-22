from app.Models.UserModel import Events
from app import db
from flask import Response, request
from datetime import datetime


def add_event():
    data = request.get_json()

    try:
        formatted_date = datetime.strptime(data["date"], "%d-%m-%Y %H:%M:%S")
    except ValueError:
        return Response("Invalid Date Format", 422)

    try:
        if Events.query.filter(Events.eventName == data["eventName"], Events.date == formatted_date).first():
            return Response("Event already exists", status=403)
        else:
            event = Events(eventName=data["eventName"], date=formatted_date)
            db.session.add(event)
            db.session.commit()
            return Response("Successfully Added Event", status=200)
    except:
        return Response("Internal Server Error", status=500)