################################################################
#   This is the Python Bank Module Used For Basic
#
#   Used For Basic Bank Solutions
#   It provides Facilities Like:
#       1. Creating New Account
#           a. Get Name For Account Holder
#           b. Get Mobile Number Of Account Holder
#           c. Get Aadhar Number Of Account Holder
#           d. Get Password From User For Accessing Account
#           e. And Create An Account With Above Details
#       2. Access Account For Following:
#           a. Add Amount
#           b. Withdraw Amount
#           c. Account Settings
#           d. Get Statement For Account
#           e. Check Current Balance
#       3.Administrative Facilities:
#           a.View Bank Accounts
#           b.Add Admins
#           c.Change Admin Passwords
################################################################

import access
import create
import datetime
import exit
import admin
import os

 
def home():
    print("Welcome To Python Bank")
    while True:
        print("""\n\n\nPress 1 to access your account
Press 2 to open new account
Press 3 for admin login
Press 4 to exit""")
        try:
            usr_ch = int(input('>> '))
            if usr_ch == 1:
                access.acc()
            elif usr_ch == 2:
                create.create_acc()
            elif usr_ch == 3:
                admin.admin()
            elif usr_ch == 4:
                exit.ext()
                break
            else:
                print('Wrong Choice!!')
        except ValueError:
            print('invalid choice')
            continue


home()
