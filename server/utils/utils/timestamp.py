import datetime

def now_ymdhms():
    return datetime.datetime.now()

def now_timestamp():
    return now_ymdhms().timestamp()

def now_timestamp_mysql():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")