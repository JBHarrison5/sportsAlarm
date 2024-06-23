from app import db


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    eventID = db.Column(db.Integer, db.ForeignKey('Events.id'), nullable=True)

    def __repr__(self):
        return f"User('{self.email}')"


