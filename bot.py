import telebot
from datetime import datetime
from config import token
from main import todayr, nextd, nextweektoday
from parser_download import download
from date import weeknum
import library as lb
import yadupload as ya
bot = telebot.TeleBot(token)
now = datetime.today().hour


@bot.message_handler(commands=["today"])
def todaym(message):
    lb.chech_user(message.chat.id)
    todayr(message, bot, lb.users[message.chat.id])
    lb.log(message)


@bot.message_handler(commands=["nextday"])
def nextdm(message):
    lb.chech_user(message.chat.id)
    nextd(message, bot, lb.users[message.chat.id])
    lb.log(message)


@bot.message_handler(commands=["week"])
def todweek(message):
    lb.chech_user(message.chat.id)
    lb.log(message)
    msg = []
    for i in range(0, 6):
        msg.append(todayr(message, None, lb.users[message.chat.id], i))
    bot.send_message(message.chat.id, ''.join(msg))


@bot.message_handler(commands=["nextweek"])
def next_week(message):
    lb.chech_user(message.chat.id)
    lb.log(message)
    msg = []
    for i in range(0, 6):
        msg.append(nextweektoday(message, None, lb.users[message.chat.id], i))
    bot.send_message(message.chat.id, ''.join(msg))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, {}! Я бот, который знает твое расписание. Напиши /help, чтобы узнать '
                                      'больше о командах'.format(message.chat.first_name))
    lb.chech_user(message.chat.id)
    lb.log(message)

@bot.message_handler(commands=['time'])
def send_time(message):
    lb.chech_user(message.chat.id)
    a = datetime.today()
    bot.send_message(message.chat.id, text='Weeknumber = ' + str(weeknum()) + ', date - ' + str(a))
    del a
    lb.log(message)


@bot.message_handler(commands=['help'])
def send_help(message):
    lb.chech_user(message.chat.id)
    if message.chat.id != 526752662:
        bot.send_message(message.chat.id,
                         'Напиши /today чтобы увидеть расписание на сегодня или /nextday - для завтрашнего дня. '
                         'Напиши /week чтобы увидеть расписание на текущую неделю или /nextweek для следующей. Чтобы '
                         'изменить текущую '
                         'группу введите номер группы от 1 до 6. Пример "1" = БАСО-01-19 (проверяйте номер группы! Иногда случаются сбросы БД)')
    else:
        bot.send_message(message.chat.id,
                         'Напиши /today чтобы увидеть расписание на сегодня или /nextday - для завтрашнего дня. '
                         'Напиши /week чтобы увидеть расписание на текущую неделю ил /nextweek для слудующей.'
                         ' /update - обновление файлов, /time - узнать текущее время время. Чтобы изменить текущую '
                         'группу введите номер группы от 1 до 6. Пример "1" = БАСО-01-19. /getlog - получить логи')
    lb.log(message)


@bot.message_handler(commands=['getlog'])
def send_logs(message):
    f = open('logs.txt', 'rb')
    bot.send_document(message.chat.id,  f)
    f.close()
    f = open('users_db.txt', 'rb')
    bot.send_document(message.chat.id, f)
    f.close()
    lb.log(message)

@bot.message_handler(commands=['update'])
def upd_rp(message):
    lb.chech_user(message.chat.id)
    if download() == 2:
        bot.reply_to(message, 'Хьюстон, у нас проблемы! Файл отсутсвует')
    else:
        bot.reply_to(message, 'Окей, Босс! Все обновлено')
    lb.log(message)


@bot.message_handler(content_types='text')
def change_gr(message):
    #try, group of excepts, else, finally
    try:
        number = int(message.text)
        if number > 6 or number < 1:
            raise ValueError("wrong number")
    except ValueError:
        bot.reply_to(message, 'Неправильное значение, введите еще раз')
    else:
        bot.reply_to(message, 'Ваща группа изменена на БАСО-0{}-19'.format(number))
        lb.users[message.chat.id] = number
        lb.zapoln_file(message.chat.id)
        lb.zapoln_db()
    lb.log(message)


if __name__ == '__main__':
    try:
        ya.download_from_disk()
        lb.zapoln_db()
        bot.infinity_polling()
    except:
        bot.send_message(526752662, 'Error')
        f = open('logs.txt', 'rb')
        bot.send_document(526752662, f)
        f.close()
