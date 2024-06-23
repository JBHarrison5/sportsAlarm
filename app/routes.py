from app import app, db
from app.Functions.register import register
from app.Functions.login import login
from app.Functions.addEvent import add_event
from app.Functions.getEvents import get_events

app.add_url_rule("/register", "register", lambda: register(), methods=["POST"])

app.add_url_rule("/login", "login", lambda: login(), methods=["POST"])

app.add_url_rule("/addEvent", "addEvent", lambda: add_event(), methods=["POST"])

app.add_url_rule("/getEvent", "getEvents", lambda: get_events(), methods=["GET"])


@app.route("/setAlarm")
def set_alarm():
    return "<h1>In set alarm route</h1>"
# Method for user to set alarm to active in the database


@app.route("/alert")
def alert():
    return "<h1>In alert route</h1>"
# Method to check whether the alert has been set to getting good

