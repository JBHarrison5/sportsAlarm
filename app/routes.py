from app import app, db
from app.Functions.register import register
from app.Functions.login import login
from app.Functions.addEvent import add_event
from app.Functions.getEvents import get_events
from app.Functions.setAlarm import set_alarm
from app.Functions.alert import alert

app.add_url_rule("/register", "register", lambda: register(), methods=["POST"])

app.add_url_rule("/login", "login", lambda: login(), methods=["POST"])

app.add_url_rule("/addEvent", "addEvent", lambda: add_event(), methods=["POST"])

app.add_url_rule("/getEvent", "getEvents", lambda: get_events(), methods=["GET"])

# user can set an event alarm
app.add_url_rule("/setAlarm", "setAlarm", lambda: set_alarm(), methods=["POST"])

# Commentator triggers an alarm
app.add_url_rule("/alert", "alert", lambda: alert(), methods=["POST"])