from datetime import datetime
from flask import Response


def validate_date(date):
    try:
        return datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
    except ValueError:
        return Response("Invalid Date Format", 422)
