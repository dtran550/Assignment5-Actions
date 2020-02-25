import math
import datetime


def firstrun():
    return "success"


def areaCircle(radius):
    if (radius < 0):
        return None
    return radius * radius * math.pi


def firstLastListElem(intList):
    # If list is empty, it is treated as a boolean False, and we have it return None
    if not intList:
        return None
    return intList[0], intList[-1]


def diffTwoDates(date1, date2):
    if (isinstance(date1, datetime.date) and isinstance(date2, datetime.date)):
        # Returning a  timedelta object from
        # https://docs.python.org/2.4/lib/datetime-timedelta.html
        return abs((date2 - date1).days)
