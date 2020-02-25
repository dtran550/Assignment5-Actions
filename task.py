import math


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
