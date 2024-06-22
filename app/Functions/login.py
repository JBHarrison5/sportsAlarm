from app.Models.UserModel import Users
from flask import Response, request
from app import db, bcrypt


def login():
    data = request.get_json()
    try:
        user = db.session.query(Users).filter(Users.email == data["email"]).first()
        if user and bcrypt.check_password_hash(user.password, data["password"]):
            return Response("Successful Log In", status=200)
        else:
            return Response("Incorrect Credentials", status=403)
    except:
        return Response("Internal Server Error", status=500)
