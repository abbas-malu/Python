import os

from systemFiles import addBook, first_run, issueBook, viewBooks,addMember,settings
from systemFiles.dataObjects import *


def main():
    usr_ch = 0
    while usr_ch != 4 or usr_ch != 5:
        print('\n\n------Welcome To Library Management System------')
        if os.path.exists('AppDetails') and os.path.exists('adminArea') and os.path.exists('booksArea') and os.path.exists('membersZone') and os.path.exists('bookIssue'):
            if not(Admin.isAdminLogged()[0]):
                print("Enter Admin Id:")
                admin_id = input('>> ')
                print("Enter Admin Password:")
                password_id = input('>> ')
                if Admin.isAdminValid(admin_id, password_id)[0]:
                    print(
                        f'\nWelcome {Admin.isAdminValid(admin_id,password_id)[1]}')
                    print(f'\nWelcome {Admin.isAdminLogged()[1]}')
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
                1 to Go to Masters
                2 to issue Books
                3 to Add Members
                4 to exit and logout
                5 to exit without logging out''')
                usr_ch = int(input('>> '))
                if usr_ch == 1:
                    addBook.addNewBook(Admin.isAdminLogged()[1])
                    print('Book Added Successfully')
                    continue
                elif usr_ch == 2:
                    viewBooks.listBooks()
                    continue
                elif usr_ch == 3:
                    issueBook.issueBook()
                    continue
                elif usr_ch == 4:
                    Admin.logout()
                elif usr_ch == 5:
                    print('Have a great day ahead!!')
                    exit()
                else:
                    print("Wrong Choice!!!")
                    continue
                break
        else:
            print("\n\nIt seems that you are using this app for the first time so you have to start setup by pressing 'f' or \nyour Library Management System requires a repair so press 'F' to repair.\nNote:This repair will delete all data and reset settings to default.")
            stp_ch = input('>> ').lower()
            if stp_ch == 'f':
                first_run.firstRun()
            else:
                print("Invalid Choice!!")


if __name__ == "__main__":
    main()
