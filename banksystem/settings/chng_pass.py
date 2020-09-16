import xlrd
import openpyxl


def password_change(acc_no):
    pass_acc = xlrd.open_workbook('account\{}.xlsx'.format(acc_no))
    pass_sheet = pass_acc.sheet_by_name('maindata')
    usr_name = pass_sheet.cell_value(0, 0)
    acc_open = openpyxl.load_workbook('account\{}.xlsx'.format(acc_no))
    worksheet = acc_open['maindata']
    prev_pass1 = pass_sheet.cell_value(2, 0)
    prev_pass2 = worksheet.cell(3, 1)
    print('Hey {}, Enter Your Current Password :'.format(usr_name))
    curr_pass = input('>> ')
    while curr_pass != prev_pass1:
        print('Wrong Password. Try Again')
        curr_pass = input('>> ')
    else:
        print('Enter New Password')
        new_pass = input('>> ')
        prev_pass2.value = new_pass
        acc_open.save('account\{}.xlsx'.format(acc_no))
    print('Hey {}, Your password is successfully updated.'.format(usr_name))
