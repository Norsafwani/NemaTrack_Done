from datetime import datetime, timedelta


def timestampTodatetime(timestamp):
    timestamp = int(timestamp)
    datetime1 = datetime.fromtimestamp(timestamp)
    return datetime1
    
def unixtime():
    ts = int(time.time())
    ts = str(ts)
    return ts

class Dict(defaultdict):
    def __init__(self):
        defaultdict.__init__(self, Dict)
    def __repr__(self):
        return dict.__repr__(self)

def last10minutes():
    now = datetime.now() - relativedelta(minutes=10)
    n1 = str(now).split('.')
    datetime2 = n1[0]
    return datetime2

def strdatetimeToDatetime(strdate):
    datetime2 = datetime.strptime(strdate, '%Y-%m-%d %H:%M:%S')
    return datetime2

def getnow():
    now = datetime.now()
    n1 = str(now).split('.')
    datetime2 = datetime.strptime(n1[0], '%Y-%m-%d %H:%M:%S')
    return datetime2
