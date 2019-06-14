import datetime


def add(moment):
    """Calculate the moment when someone has lived for 10^9 seconds"""
    return moment +  datetime.timedelta(seconds=10 ** 9)
