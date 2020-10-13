import yadisk
from math import fabs
import os
import datetime
import time
from config import tokenya
from main import update

y = yadisk.YaDisk(token=tokenya)
time0 = datetime.datetime.now()

def upload_to_disk():
    now = datetime.datetime.now()
    global time0
    delta = now - time0
    delta_in_s = delta.total_seconds()
    hours = divmod(delta_in_s, 3600)[0]
    if fabs(hours) > 1:
        time0 = datetime.datetime.now()
        try:
            y.upload('logs.txt', '/bot/logs.txt')
            y.upload('users_db.txt', '/bot/users_db.txt')
            y.upload('Raspisanie.xlsx', '/bot/Raspisanie.xlsx')
        except yadisk.exceptions.PathExistsError:
            y.remove('/bot/logs.txt')
            y.remove('/bot/users_db.txt')
            y.remove('/bot/Raspisanie.xlsx')
            time.sleep(2)
            print("Still waiting...")
            y.upload('logs.txt', '/bot/logs.txt')
            y.upload('users_db.txt', '/bot/users_db.txt')
            y.upload('Raspisanie.xlsx', '/bot/Raspisanie.xlsx')
    # try:
    #     y.upload('logs.txt', '/bot/logs.txt')
    #     y.upload('users_db.txt', '/bot/users_db.txt')
    # except yadisk.exceptions.PathExistsError:
    #     y.remove('/bot/logs.txt')
    #     y.remove('/bot/users_db.txt')
    #     time.sleep(5)
    #     print("Still waiting...")
    #     y.upload('logs.txt', '/bot/logs.txt')
    #     y.upload('users_db.txt', '/bot/users_db.txt')
    # except yadisk.exceptions.ResourceIsLockedError:
    #     time.sleep(5)
    #     print("Still waiting...")
    # if y.exists('/bot/logs.txt'):
    #     y.remove('/bot/logs.txt', permanently=True)
    #     y.remove('/bot/users_db.txt', permanently=True)
    #     y.upload('logs.txt', '/bot/logs.txt')
    #     y.upload('users_db.txt', '/bot/users_db.txt')
    #     print('deleted')
    # else:
    #     y.upload('logs.txt', '/bot/logs.txt')
    #     y.upload('users_db.txt', '/bot/users_db.txt')


def download_from_disk():
    if os.path.exists('logs.txt'):
        os.remove('logs.txt')
    if os.path.exists('users_db.txt'):
        os.remove('users_db.txt')
    if os.path.exists('Raspisanie.xlsx'):
        os.remove('Raspisanie.xlsx')

    y.download('/bot/logs.txt', 'logs.txt')
    y.download('/bot/users_db.txt', 'users_db.txt')
    y.download('/bot/Raspisanie.xlsx', 'Raspisanie.xlsx')
    update()
