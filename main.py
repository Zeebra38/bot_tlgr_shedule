from openpyxl import load_workbook
from datetime import date, timedelta, datetime, time
from date import weeknum, getweekday
from util import zapoln
from objects import Obj, Day
import os


def update():
    #if not os.path.isfile('Rasp.txt'):
    f = open('Baso-01.txt', 'w', encoding='utf8', errors='ignore')
    f1 = open('Baso-02.txt', 'w', encoding='utf8', errors='ignore')
    f2 = open('Baso-03.txt', 'w', encoding='utf8', errors='ignore')
    f3 = open('Baso-04.txt', 'w', encoding='utf8', errors='ignore')
    f4 = open('Baso-05.txt', 'w', encoding='utf8', errors='ignore')
    f5 = open('Baso-06.txt', 'w', encoding='utf8', errors='ignore')
    wb = load_workbook('./Raspisanie.xlsx')
    sheet = wb.get_sheet_by_name('Лист1')
    zapoln(f, sheet, 1)
    zapoln(f1, sheet, 2)
    zapoln(f2, sheet, 3)
    zapoln(f3, sheet, 4)
    zapoln(f4, sheet, 5)
    zapoln(f5, sheet, 6)
    f.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()


def todayr(message, bot=None, group=1, dayweek=-1):
    b = Day()
    f = open('Baso-0{}.txt'.format(group), 'r', encoding='utf8', errors='ignore')
    if dayweek == -1:
        today = datetime.today().weekday()
    else:
        today = dayweek
    pos = 0
    if today == 0:
        for line in f:
            pos += len(line)
            if line == 'Понедельник:\n':
                break
    elif today == 1:
        for line in f:
            pos += len(line)
            if line == 'Вторник:\n':
                break
    elif today == 2:
        for line in f:
            pos += len(line)
            if line == 'Среда:\n':
                break
    elif today == 3:
        for line in f:
            pos += len(line)
            if line == 'Четверг:\n':
                break
    elif today == 4:
        for line in f:
            pos += len(line)
            if line == 'Пятница:\n':
                break
    elif today == 5:
        for line in f:
            pos += len(line)
            if line == 'Суббота:\n':
                break
    elif today == 6:
        if bot is not None:
            bot.send_message(message.chat.id, 'Сегодня воскресенье, пар нет')
        else:
            return 'Сегодня воскресенье, пар нет'
        return
    k = 0
    for line in f:
        if k == 12:
            break
        else:
            k += 1
        b.objs.append(Obj(line, weeknum()))
    if bot is not None:
        buf = 'Группа - 0{} '.format(group) + b.show(weeknum(), today)
        bot.send_message(message.chat.id, buf)
    else:
        buf = b.show(weeknum(), today)
        if buf == 'Сегодня пар нет':
            return 'Группа - 0{} '.format(group) + getweekday(today) + ' ' + str(weeknum()) + ' неделя\n' + buf + 2*'\n'
        else:
            return 'Группа - 0{} '.format(group) + buf + '\n'
    del b
    f.close()


def nextweektoday(message, bot=None, group=1, dayweek=-1):
    b = Day()
    f = open('Baso-0{}.txt'.format(group), 'r', encoding='utf8', errors='ignore')
    if dayweek == -1:
        today = datetime.today().weekday()
    else:
        today = dayweek
    pos = 0
    if today == 0:
        for line in f:
            pos += len(line)
            if line == 'Понедельник:\n':
                break
    elif today == 1:
        for line in f:
            pos += len(line)
            if line == 'Вторник:\n':
                break
    elif today == 2:
        for line in f:
            pos += len(line)
            if line == 'Среда:\n':
                break
    elif today == 3:
        for line in f:
            pos += len(line)
            if line == 'Четверг:\n':
                break
    elif today == 4:
        for line in f:
            pos += len(line)
            if line == 'Пятница:\n':
                break
    elif today == 5:
        for line in f:
            pos += len(line)
            if line == 'Суббота:\n':
                break
    elif today == 6:
        if bot is not None:
            bot.send_message(message.chat.id, 'Сегодня воскресенье, пар нет')
        else:
            return 'Сегодня воскресенье, пар нет'
        return
    k = 0
    for line in f:
        if k == 12:
            break
        else:
            k += 1
        b.objs.append(Obj(line, weeknum()+1))
    if bot is not None:
        buf = 'Группа - 0{} '.format(group) + b.show(weeknum()+1, today)
        bot.send_message(message.chat.id, buf)
    else:
        buf = b.show(weeknum()+1, today)
        if buf == 'Сегодня пар нет':
            return 'Группа - 0{} '.format(group) + getweekday(today) + ' ' + str(weeknum()+1) + ' неделя\n' + buf + 2*'\n'
        else:
            return 'Группа - 0{} '.format(group) + buf + '\n'
    del b
    f.close()


def nextd(message, bot, group):
    b = Day()
    f = open('Baso-0{}.txt'.format(group), 'r', encoding='utf8', errors='ignore')
    today = datetime.today().weekday() + 1
    if today == 7:
        today = 0
    pos = 0
    if today == 0:
        for line in f:
            pos += len(line)
            if line == 'Понедельник:\n':
                break
    elif today == 1:
        for line in f:
            pos += len(line)
            if line == 'Вторник:\n':
                break
    elif today == 2:
        for line in f:
            pos += len(line)
            if line == 'Среда:\n':
                break
    elif today == 3:
        for line in f:
            pos += len(line)
            if line == 'Четверг:\n':
                break
    elif today == 4:
        for line in f:
            pos += len(line)
            if line == 'Пятница:\n':
                break
    elif today == 5:
        for line in f:
            pos += len(line)
            if line == 'Суббота:\n':
                break
    elif today == 6:
        bot.send_message(message.chat.id, 'Завтра воскресенье, пар нет')
        return
    k = 0
    for line in f:
        if k == 12:
            break
        else:
            k += 1
        if today == 0:
            b.objs.append(Obj(line, weeknum() + 1))
        else:
            b.objs.append(Obj(line, weeknum()))
    if today == 0:
        buf = 'Группа - 0{} '.format(group) + b.show(weeknum() + 1, today)
        bot.send_message(message.chat.id, buf)
    else:
        buf = 'Группа - 0{} '.format(group) + b.show(weeknum(), today)
        bot.send_message(message.chat.id, buf)
    f.close()

