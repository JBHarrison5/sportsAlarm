from flask import request, Response, jsonify
from app.Models.EventModel import Events
from app.Models.UserModel import Users
from app import db
from sqlalchemy import update
from datetime import datetime


class EventController:
    @staticmethod
    def get_events():
        user_id = request.args.get('userID')
        event_id = request.args.get('eventID')

        if not user_id and not event_id:
            events = Events.query.all()
            return jsonify([(event.obj_to_dict()) for event in events])
        elif user_id and not event_id:
            events = db.session.query(Events).join(Users, Users.eventID == Events.id).filter(
                Users.id == user_id).all()
            return jsonify([(event.obj_to_dict()) for event in events])
        elif not user_id and event_id:
            event = db.session.query(Events).filter(Events.id == event_id).first()
            return jsonify(event.obj_to_dict())
        else:
            return Response("Invalid Parameters", status=422)

    @staticmethod
    def alert():
        data = request.get_json()
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

    @staticmethod
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
