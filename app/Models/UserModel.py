from app import db


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    eventID = db.Column(db.Integer, db.ForeignKey('Events.id'), nullable=True)

    def __repr__(self):
        return f"User('{self.email}')"


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