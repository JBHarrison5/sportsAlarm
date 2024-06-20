from app.Models.UserModel import User
from app import db
from flask import Response, request


def register():
    data = request.get_json()
    try:
        if User.query.filter_by(email=data["email"]).first():
            return Response("User already exists", status=403)
        else:
            user = User(email=data["email"], password=data["password"])
            db.session.add(user)
            db.session.commit()
            return Response("Successfully Registered User", status=200)
    except:
        return Response("Internal Server Error", status=500)