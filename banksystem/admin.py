import json
from admin_acc import add_usr, chng_pass, view_acc

def admin():
    admin_usr = input('Enter Admin User Name: ')
    admin_pswd = input('Enter Admin Password: ')
    admin_json = open('account\\admin.json', 'r')
    admin_data = json.load(admin_json)
    admin_usrs = admin_data['admin_list']
    admin_exst = False
    for myAdmin in admin_usrs:
         if (myAdmin['admin_usr'] == admin_usr) & (myAdmin['admin_pswd'] == admin_pswd):
             admin_exst = True
         else:
             continue
    if admin_exst:
        while True:
            print('Welcome {}'.format(admin_usr))
            print("""
Press
1 to view accounts in the bank
2 to add admin user
3 to change password for current admin.
4 to exit""")
            try:
                admin_ch = int(input(">>"))
                if admin_ch == 1:
                    view_acc.view_acc()
                elif admin_ch == 2:
                    add_usr.add_usr()
                elif admin_ch == 3:
                    chng_pass.chng_pass(admin_usr)
                else:
                    print('Thanks Admin {}'.format(admin_usr))
                    break
            except ValueError:
                print('Invalid Choice')
                continue
    else:
        print('No User Exists Or Invalid Details')
    admin_json.close()