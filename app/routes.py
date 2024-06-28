from app import app

from app.Controllers.EventController import EventController
from app.Controllers.UserController import UserController

app.add_url_rule("/register", "register", lambda: UserController.register(), methods=["POST"])

app.add_url_rule("/login", "login", lambda: UserController.login(), methods=["POST"])

app.add_url_rule("/addEvent", "addEvent", lambda: EventController.add_event(), methods=["POST"])

app.add_url_rule("/getEvent", "getEvents", lambda: EventController.get_events(), methods=["GET"])

# user can set an event alarm
app.add_url_rule("/setAlarm", "setAlarm", lambda: UserController.set_alarm(), methods=["POST"])

# Commentator triggers an alarm
app.add_url_rule("/alert", "alert", lambda: EventController.alert(), methods=["POST"])