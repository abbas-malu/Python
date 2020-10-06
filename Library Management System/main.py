import os
from first_run import firstRun
from dataObjects import *


def main():
    while True:
        print('------Welcome To Library Management System------')
        if os.path.exists('AppDetails') and os.path.exists('adminArea') and os.path.exists('booksArea') and os.path.exists('membersZone') and os.path.exists('bookIssue'):
            if not(Admin.isAdminLogged()[0]):
                print("Enter Admin Id:")
                admin_id = input('>> ')
                print("Enter Admin Password:")
                password_id = input('>> ')
                if Admin.isAdminValid(admin_id, password_id)[0]:
                    print(f'Welcome {Admin.isAdminValid(admin_id,password_id)[1]}')
                    print(f'Welcome {Admin.isAdminLogged()[1]}')
                    print('''Press
                    1 to Add Books
                    2 to issue Books
                    3 to Add Members
                    4 to Go to Settings
                    5 to exit and logout
                    6 to exit without logging out''')
                    break
                else:
                    print(Admin.isAdminValid(admin_id, password_id)[1])
            else:
                print(f'Welcome {Admin.isAdminLogged()[1]}')
                print('''Press
                1 to Add Books
                2 to issue Books
                3 to Add Members
                4 to Go to Settings
                5 to exit and logout
                6 to exit without logging out''')
                usr_ch = int(input('>> '))
                if usr_ch==1:
                    pass
                elif usr_ch==2:
                    pass
                elif usr_ch==3:
                    pass
                elif usr_ch==4:
                    pass
                elif usr_ch==5:
                    Admin.logout()
                elif usr_ch==6:
                    print('Have a great day ahead!!')
                    exit()
                break
        else:
            print("It seems that you are using this app for the first time so you have to start setup by pressing 'f' or \nyour Library Management System requires a repair so press 'F' to repair.\nNote:This repair will delete all data and reset settings to default.")
            stp_ch = input('>> ').lower()
            if stp_ch == 'f':
                firstRun()
            else:
                print("Invalid Choice!!")


if __name__ == "__main__":
    main()
