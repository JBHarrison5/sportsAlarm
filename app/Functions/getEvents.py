from app.Models.UserModel import Events, db, Users
from flask import jsonify, request, Response


def get_events():
    user_id = request.args.get('userID')
    event_id = request.args.get('eventID')

    if not user_id and not event_id:
        events = Events.query.all()
        return jsonify([(event.obj_to_dict()) for event in events])
    elif user_id and not event_id:
        events = db.session.query(Events).join(Users, Users.eventID == Events.id).filter(Users.id == user_id).all()
        return jsonify([(event.obj_to_dict()) for event in events])
    elif not user_id and event_id:
        event = db.session.query(Events).filter(Events.id == event_id).first()
        return jsonify(event.obj_to_dict())
    else:
        return Response("Invalid Parameters", status=422)

