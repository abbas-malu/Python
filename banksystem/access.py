import xlrd
import os
from acs_acc import add,acc_set,balance,withdraw,state_gen
def acc():
    act_no = input("Enter Your Account No. : ").lower()
    if os.path.exists('account\{}.xlsx'.format(act_no)):
        pswd = input('Enter Password : ')
        acc_file = xlrd.open_workbook('account\{}.xlsx'.format(act_no))
        mn_sheet = acc_file.sheet_by_name('maindata')
        pswd_org = mn_sheet.cell_value(2,0)
        acc_ch = 0
        while acc_ch != 6:
            if pswd == pswd_org:
                name = mn_sheet.cell_value(0,0)
                print('Welcome {}'.format(name))
                print('''Press
    1 for checking balance 
    2 for withdrawing money
    3 for adding money
    4 for statement
    5 for account setting
    6 for going back''')
                acc_ch = int(input('>> '))
                if acc_ch == 1:
                    balance.chk_bal(act_no)
                elif acc_ch == 2:
                    withdraw.withdraw(act_no)
                elif acc_ch == 3:
                    add.add(act_no)
                elif acc_ch == 4:
                    state_gen.stat_gen(act_no)
                elif acc_ch == 5:
                    acc_set.setting(act_no)
                else:
                    print('Wrong Choice')
            else:
                print('Wrong Password!!')
                break
    else:
        print('This Account Does Not Exists')