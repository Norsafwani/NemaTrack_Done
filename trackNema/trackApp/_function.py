
from datetime import datetime


def strdatetimeToDatetime(strdate):
    datetime2 = datetime.strptime(strdate, '%Y-%m-%d %H:%M:%S')
    return datetime2