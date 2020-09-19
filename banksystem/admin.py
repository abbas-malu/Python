import json


def admin():
    admin_usr = input('Enter Admin User Name: ')
    admin_pswd = input('Enter Admin Password: ')
    admin_json = open('account\\admin.json', 'r')
    admin_data = json.load(admin_json)
    if (admin_data['admin_usr']==admin_usr) & (admin_data['admin_pswd']==admin_pswd):
        print('Welcome Admin')