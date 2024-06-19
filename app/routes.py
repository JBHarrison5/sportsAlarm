from app import app, db
from app.Functions.register import register

json = {
    "email": "john@.com",
    "password": "securepassword123"
}
app.add_url_rule("/register", "register", lambda: register(json))


@app.route("/login")
def login():
    return "<h1>In login route</h1>"
# Method for logging in


@app.route("/addEvent")
def add_event():
    return "<h1>In add Event route</h1>"
# Method for add Event


@app.route("/getAllEvents")
def get_all_events():
    return "<h1>In get all events route</h1>"
# Method for get all events


@app.route("/getUsersEvents")
def get_users_events():
    return "<h1>In get Users Events route</h1>"
# Method for getting events for specific users


@app.route("/getSpecificEvents")
def get_specific_events():
    return "<h1>In get Specific Events route</h1>"
# Method for getting specific event


@app.route("/setAlarm")
def set_alarm():
    return "<h1>In set alarm route</h1>"
# Method for user to set alarm to active in the database


@app.route("/alert")
def alert():
    return "<h1>In alert route</h1>"
# Method to check whether the alert has been set to getting good

