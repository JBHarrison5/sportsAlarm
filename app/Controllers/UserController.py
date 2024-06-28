from flask import request, Response
from app.Models.UserModel import Users
from app.Models.EventModel import Events
from app import db, bcrypt
from sqlalchemy import update


class UserController:
    @staticmethod
    def register():
        data = request.get_json()

        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            return Response("Invalid JSON Format", 422)

        if Users.query.filter_by(email=email).first():
            return Response("User already exists", status=403)
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Users(email=data["email"], password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return Response("Successfully Registered User", status=200)

    @staticmethod
    def login():
        data = request.get_json()

        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            return Response("Invalid JSON Format", 422)

        user = db.session.query(Users).filter(Users.email == email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return Response("Successful Log In", status=200)
        else:
            return Response("Incorrect Credentials", status=403)

    @staticmethod
    def set_alarm():
        data = request.get_json()

        try:
            user_id = data["userID"]
            event_id = data["eventID"]
        except KeyError:
            return Response("Invalid JSON Format", 422)

        if Users.query.filter(Users.id == user_id).first() and Events.query.filter(Events.id == event_id).first():
            statement = update(Users).where(Users.id == user_id).values(eventID=event_id)
            db.session.execute(statement)
            db.session.commit()
            return Response("Successfully Added Alarm", status=200)
        else:
            return Response("Event or User does not exist", status=404)
