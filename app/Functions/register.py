from app.Models.UserModel import Users
from app import db, bcrypt
from flask import Response, request


def register():
    data = request.get_json()
    try:
        if Users.query.filter_by(email=data["email"]).first():
            return Response("User already exists", status=403)
        else:
            hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
            user = Users(email=data["email"], password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return Response("Successfully Registered User", status=200)
    except:
        return Response("Internal Server Error", status=500)