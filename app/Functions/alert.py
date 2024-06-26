from flask import request, Response
from app.Models.EventModel import Events
from sqlalchemy import update
from app import db


def alert():
    data = request.get_json()
    print(data)
    try:
        event_id = data["eventID"]
    except KeyError:
        return Response("Invalid JSON Format", 422)

    if Events.query.filter(Events.id == event_id).first():
        statement = update(Events).where(Events.id == event_id).values(wakeUp=True)
        db.session.execute(statement)
        db.session.commit()
        return Response("Successfully Set Alert", status=200)
    else:
        return Response("Event does not exist", status=404)
