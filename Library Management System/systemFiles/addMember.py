import json
import os

from .dataObjects import Member

def AddMember():
    """
    Adding A Member
    """
    memName = input('Enter Name of member: ')
    memMob = ''
    while len(memMob)!=10:
        memMob = input('Enter 10 digit Mobile No: ')
    memType = ''
    while memType != 'Gold' and memType != 'Silver':
        memType = input('Enter membership type (Gold or Silver): ').capitalize()
        if memType != 'Gold' or memType != 'Silver':
            print('Enter valid membership type (First letter should be capital)')
    newMember = Member(memName,memMob,memType)
    newMember.save()
