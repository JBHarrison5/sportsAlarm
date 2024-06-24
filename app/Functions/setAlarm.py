from app.Models.UserModel import Users
from app.Models.EventModel import Events
from flask import Response, request
from datetime import datetime
from sqlalchemy import update
from app import db


def set_alarm():
    data = request.get_json()

    try:
        userID = data["userID"]
        eventID = data["eventID"]
    except KeyError:
        return Response("Invalid JSON Format", 422)

    if Users.query.filter(Users.id == userID).first() and Events.query.filter(Events.id == eventID).first():
        statement = update(Users).where(Users.id == userID).values(eventID=eventID)
        db.session.execute(statement)
        db.session.commit()
        return Response("Successfully Added Alarm", status=200)
    else:
        return Response("Event or User does not exist", status=404)
