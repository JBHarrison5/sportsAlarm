from app import app, db
from app.Functions.register import register
from app.Functions.login import login
from app.Functions.addEvent import add_event
from app.Functions.getEvents import get_events
from app.Functions.setAlarm import set_alarm

app.add_url_rule("/register", "register", lambda: register(), methods=["POST"])

app.add_url_rule("/login", "login", lambda: login(), methods=["POST"])

app.add_url_rule("/addEvent", "addEvent", lambda: add_event(), methods=["POST"])

app.add_url_rule("/getEvent", "getEvents", lambda: get_events(), methods=["GET"])

app.add_url_rule("/setAlarm", "setAlarm", lambda: set_alarm(), methods=["POST"])


@app.route("/alert")
def alert():
    return "<h1>In alert route</h1>"
# Method to check whether the alert has been set to getting good

