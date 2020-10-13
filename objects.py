import re
from datetime import time


class Obj:
    order = 0
    times = time()
    timee = time()
    week = 0
    nazv = ''
    type = ''
    prepod = ''
    cab = ''

    def nazvput(self, s, week):
        v = s.replace(' ', '')
        v = v.replace(',', '')
        if v.isalnum() and (v.isalpha() is False):
            pattern = r'кр\d'
            result = re.match(pattern, v)
            if result == None:
                b = s
                b = b.replace('.', ',')
                a = [m.start() for m in re.finditer(str(week), b)]
                for pos in a:
                    if (b[pos - 1] == ',' or b[pos - 1] == '@' or pos == 0) and (
                            b[pos + 1] == ',' or b[pos + 2] == ','):
                        return b
                return 'Ничего'
            else:
                b = s
                b = b.replace('.', ',')
                a = [m.start() for m in re.finditer(str(week), b)]
                for pos in a:
                    if (b[pos - 1] == ',' or b[pos - 1] == 'р' or b[pos - 1] == '@' or pos == 0) and (
                            b[pos + 1] == ',' or b[pos + 2] == ',' or True if b[pos + 1].isalph() or b[
                                pos + 2].isalph() else False):
                        return 'Ничего'
                return b

        elif v.isalpha():
            return s
        elif v.find('!') != -1:
            v = s
            v = v.replace('.', ',')
            b = v.find('@')
            a = [m.start() for m in re.finditer(str(week), v)]
            for pos in a:
                if (v[pos - 1] == ',' or v[pos - 1] == '@' or v[pos - 1] == '!') and (
                        v[pos + 1] == ',' or v[pos + 2] == ','):
                    if pos > b:
                        d = s[b + 1:]
                        return d
                    else:
                        d = s[1:b]
                        return d
            return 'Ничего'

    def typeput(self, s, nazv, week):
        nazv = nazv.replace('.', ',')
        if s.find('!') == -1:
            return s
        else:
            b = nazv.find('@')
            a = [m.start() for m in re.finditer(str(week), nazv)]
            for pos in a:
                if (nazv[pos - 1] == ',' or nazv[pos - 1] == '@' or nazv[pos - 1] == '!') and (
                        nazv[pos + 1] == ',' or nazv[pos + 2] == ','):
                    if pos > b:
                        v = s[s.find('@') + 1:]
                        return v
                    else:
                        v = s[1:s.find('@')]
                        return v

    def __init__(self, s, week):
        v = s.split('+')
        self.order = int(v[0])
        if self.order == 1:
            self.times = time(9, 0)
            self.timee = time(10, 30)
        elif self.order == 2:
            self.times = time(10, 40)
            self.timee = time(12, 10)
        elif self.order == 3:
            self.times = time(12, 40)
            self.timee = time(14, 10)
        elif self.order == 4:
            self.times = time(14, 20)
            self.timee = time(15, 50)
        elif self.order == 5:
            self.times = time(16, 20)
            self.timee = time(17, 50)
        elif self.order == 6:
            self.times = time(18, 0)
            self.timee = time(19, 30)
        elif self.order == 7:
            self.times = time(19, 40)
            self.timee = time(21, 10)
        if v[1] == 'I':
            self.week = 1
        else:
            self.week = 2
        self.nazv = self.nazvput(v[2], week)
        self.nazv = str(self.nazv)
        self.nazv = self.nazv.replace('.', ',')
        self.type = self.typeput(v[3], v[2], week)
        if v[4] == 'Ничего':
            self.prepod = '---'
        else:
            self.prepod = v[4]
        if v[5].isalnum():
            self.cab = v[5]
        else:
            self.cab = v[5].replace('@', ' ')
            self.cab = self.cab.replace('!', ' ')
        if self.cab == 'Ничего':
            self.cab = '--'


class Day:
    maxnaz = 0
    maxprepod = 0
    weekday = ''
    objs = []
    todobj = []

    def show(self, week, today):
        if today == 0:
            self.weekday = 'Понедельник'
        elif today == 1:
            self.weekday = 'Вторник'
        elif today == 2:
            self.weekday = 'Среда'
        elif today == 3:
            self.weekday = 'Четверг'
        elif today == 4:
            self.weekday = 'Пятница'
        elif today == 5:
            self.weekday = 'Суббота'
        for obj in self.objs:
            if week % 2 == 0 and obj.week % 2 == 0:
                self.todobj.append(obj)
            elif week % 2 == 1 and obj.week == 1:
                self.todobj.append(obj)
        k = 6
        for obj in self.todobj:
            if obj.nazv == 'Ничего':
                k -= 1
            else:
                if len(obj.nazv) > self.maxnaz:
                    self.maxnaz = len(obj.nazv)
                if len(obj.prepod) > self.maxprepod:
                    self.maxprepod = len(obj.prepod)
        if k == 0:
            rez = 'Сегодня пар нет'
            self.todobj.clear()
            self.maxnaz = 0
            self.maxprepod = 0
            self.objs.clear()
            return rez
        k = 0
        rez = self.weekday + ' ' + str(week) + ' неделя :\n'
        for obj in self.todobj:
            k += 1
            if obj.nazv == 'Ничего':
                rez += str(obj.order) + ' ' + str(obj.times)[0:len(str(obj.times)) - 3] + '-' + str(obj.timee)[0:len(
                    str(obj.timee)) - 3] + '  --------\n'
            else:
                # buf = obj.nazv.ljust(self.maxnaz, ' ')
                # buf1 = obj.prepod.ljust(self.maxprepod, ' ')
                rez += str(obj.order) + ' ' + str(obj.times)[0:len(str(obj.times)) - 3] + '-' + str(obj.timee)[0:len(
                    str(obj.timee)) - 3] + ' ' + obj.nazv + ' ' + obj.type + ' ' + obj.prepod + ' ' + str(
                    obj.cab) + '\n'
        if k < 6:
            for c in range(k, 7):
                rez += '--------\n'
        self.todobj.clear()
        self.maxnaz = 0
        self.maxprepod = 0
        self.objs.clear()
        return rez

    def show_woeveryweek(self, week, today):
        rez = ""
        if today == 0:
            self.weekday = 'Понедельник'
        elif today == 1:
            self.weekday = 'Вторник'
        elif today == 2:
            self.weekday = 'Среда'
        elif today == 3:
            self.weekday = 'Четверг'
        elif today == 4:
            self.weekday = 'Пятница'
        elif today == 5:
            self.weekday = 'Суббота'
        for obj in self.objs:
            if week % 2 == 0 and obj.week % 2 == 0:
                self.todobj.append(obj)
            elif week % 2 == 1 and obj.week == 1:
                self.todobj.append(obj)
        k = 6
        for obj in self.todobj:
            if obj.nazv == 'Ничего':
                k -= 1
            else:
                if len(obj.nazv) > self.maxnaz:
                    self.maxnaz = len(obj.nazv)
                if len(obj.prepod) > self.maxprepod:
                    self.maxprepod = len(obj.prepod)
        if k == 0:
            rez = 'Сегодня пар нет'
            return rez
        k = 0
        if self.weekday == 'Понедельник':
            rez = self.weekday + ' ' + str(week) + ' неделя :\n'
        else:
            rez = self.weekday + ':\n'
        for obj in self.todobj:
            k += 1
            if obj.nazv == 'Ничего':
                rez += str(obj.order) + ' ' + str(obj.times)[0:len(str(obj.times)) - 3] + '-' + str(obj.timee)[0:len(
                    str(obj.timee)) - 3] + '  --------\n'
            else:
                buf = obj.nazv.ljust(self.maxnaz, ' ')
                buf1 = obj.prepod.ljust(self.maxprepod, ' ')
                rez += str(obj.order) + ' ' + str(obj.times)[0:len(str(obj.times)) - 3] + '-' + str(obj.timee)[0:len(
                    str(obj.timee)) - 3] + ' ' + obj.nazv + ' ' + obj.type + ' ' + obj.prepod + ' ' + str(
                    obj.cab) + '\n'
        if k < 6:
            for c in range(k, 7):
                rez += '--------\n'
        self.todobj.clear()
        self.maxnaz = 0
        self.maxprepod = 0
        self.objs.clear()
        return rez
