from app import db
from flask import request, jsonify, Response
from sqlalchemy import update
from datetime import datetime


class Events(db.Model):
    __tablename__ = 'Events'
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(60), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    wakeUp = db.Column(db.Boolean, nullable=False, default = False)

    def __repr__(self):
        return f"Events('{self.eventName}', '{self.date})"

    def obj_to_dict(self):
        return {
            "id": self.id,
            "eventName": self.eventName,
            "date": self.date,
            "wakeUp": self.wakeUp
        }
