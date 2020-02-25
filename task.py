import math


def firstrun():
    return "success"


def areaCircle(radius):
    if (radius < 0):
        return None
    return radius * radius * math.pi
