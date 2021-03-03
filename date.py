from datetime import date, timedelta, datetime

def weeknum():
    zero = datetime(2021, 2, 8)
    now = datetime.today()
    #now = datetime(2020, 9, 22)
    delta = now - zero
    deltaweeks = 1
    #print(delta.days)
    if delta.days >= 7:
        buf = delta.days
        while buf >= 7:
            deltaweeks += 1
            buf = buf - 7
    return deltaweeks

def getweekday(today = datetime.today().weekday()):
    if today == 0:
        return 'Понедельник'
    elif today == 1:
        return 'Вторник'
    elif today == 2:
        return 'Среда'
    elif today == 3:
        return 'Четверг'
    elif today == 4:
        return 'Пятница'
    elif today == 5:
        return 'Суббота'

