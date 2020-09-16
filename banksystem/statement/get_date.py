import datetime


def date_today():
    # cur_date = datetime.date.today()
    cur_time1 = datetime.datetime.now()
    cur_date = cur_time1.strftime("%d/%m/%Y %H:%M:%S")
    return cur_date
