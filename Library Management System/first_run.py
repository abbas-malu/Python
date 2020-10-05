import os
from time import sleep

def firstRun():
    print('Initializing', end='')
    for i in range(10):
        print('.', end='')
        sleep(0.5)
    print()
    sleep(1.5)
    print('Looking for directories',end='')
    if os.path.exists('booksArea'):
        os.rmdir('booksArea')
    if os.path.exists('adminArea'):
        os.rmdir('adminArea')
    if os.path.exists('membersZone'):
        os.rmdir('membersZone')
    if os.path.exists('bookIssue'):
        os.rmdir('bookIssue')
    if os.path.exists('AppDetails'):
        os.rmdir('AppDetails')
    for i in range(10):
        print('.', end='')
        sleep(0.4)
    print()
    sleep(2)
    print('Setting up directories',end='')
    os.mkdir('booksArea')
    os.mkdir('adminArea')
    os.mkdir('adminArea/admins')
    os.mkdir('membersZone')
    os.mkdir('bookIssue')
    os.mkdir('AppDetails')
    for i in range(10):
        print('.', end='')
        sleep(0.4)
    print()
    sleep(3)
    print('Library Setup Successful.')

if __name__ == "__main__":
    firstRun()