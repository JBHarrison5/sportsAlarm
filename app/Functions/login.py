from app.Models.UserModel import Users
from flask import Response, request
from app import db, bcrypt


def login():
    data = request.get_json()

    try:
        email= data["email"]
        password = data["password"]
    except KeyError:
        return Response("Invalid JSON Format", 422)

    user = db.session.query(Users).filter(Users.email == email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return Response("Successful Log In", status=200)
    else:
        return Response("Incorrect Credentials", status=403)
