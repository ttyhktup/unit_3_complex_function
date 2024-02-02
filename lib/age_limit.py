from datetime import datetime
import math
def age_limit(date):

    age = (datetime.today() - datetime.strptime(date, "%Y-%m-%d")).days
    difference = age/365
    if math.floor(difference) < 16:
        return f"Access denied. Current age: {math.floor(difference)}. Required age: 16"
    elif math.floor(difference) >= 16:
        return "Access granted."
