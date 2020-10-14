import os,json,datetime
from .dataObjects import Admin,Book,Member


def settings(adminName):
    """
    Settings Module for library Management
    """
    print(f'\n\nWelcome to settings module, {adminName}')
    setting_ch = ''
    while type(setting_ch) != int:
        setting_ch = int(input('''Press
        1 to Add Admin
        2 to change password for current Admin
        3 to Alter Book Details
        4 to Delete Books
        
        '''))