import datetime
import json
import os
import shutil
from time import sleep

from .dataObjects import Admin


def firstRun():
    print('Initializing', end='')
    for i in range(10):
        print('.', end='')
        sleep(0.5)
    print()
    sleep(1.5)
    print('Looking for directories', end='')
    if os.path.exists('booksArea'):
        shutil.rmtree('booksArea', ignore_errors=True)
    if os.path.exists('adminArea'):
        shutil.rmtree('adminArea', ignore_errors=True)
    if os.path.exists('membersZone'):
        shutil.rmtree('membersZone', ignore_errors=True)
    if os.path.exists('bookIssue'):
        shutil.rmtree('bookIssue', ignore_errors=True)
    if os.path.exists('AppDetails'):
        shutil.rmtree('AppDetails', ignore_errors=True)
    for i in range(10):
        print('.', end='')
        sleep(0.4)
    print()
    sleep(2)
    print('Setting up directories', end='')
    os.mkdir('booksArea')
    os.mkdir('adminArea')
    os.mkdir('adminArea/admins')
    with open('adminArea/log.json', 'w') as log:
        logs = {'logged_in': False, 'username': None}
        json.dump(logs, log)
    os.mkdir('membersZone')
    os.mkdir('membersZone/members')
    os.mkdir('membersZone/members/Gold')
    os.mkdir('membersZone/members/Silver')
    os.mkdir('bookIssue')
    os.mkdir('AppDetails')
    with open('AppDetails/app_log.json', 'w') as app_log:
        logs = {'appVersion': '1.0', 'date_installed': str(
            datetime.datetime.now())}
        json.dump(logs, app_log)
    for i in range(10):
        print('.', end='')
        sleep(0.4)
    print()
    sleep(3)
    print('Library Setup Successful.')
    print('Enter following details to create new SuperUser')
    admin_name = input('Enter your name: ')
    admin_email = input('Enter your email: ')
    admin_username = input('Enter your username: ')
    admin_password = input('Enter your password: ')
    newAdmin = Admin(name=admin_name, email=admin_email,
                     username=admin_username, password=admin_password)
    newAdmin.save()


if __name__ == "__main__":
    firstRun()
