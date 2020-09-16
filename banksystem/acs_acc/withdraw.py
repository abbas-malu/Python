import xlrd
import openpyxl
from statement import stat_writer


def withdraw(acc_no):
    add_acc = xlrd.open_workbook('account\{}.xlsx'.format(acc_no))
    add_sheet = add_acc.sheet_by_name('maindata')
    cur_bal = float(add_sheet.cell_value(3, 0))
    usr_name = add_sheet.cell_value(0, 0)
    acc_open = openpyxl.load_workbook('account\{}.xlsx'.format(acc_no))
    worksheet = acc_open['maindata']
    amt_cell = worksheet.cell(4, 1)
    print('Hey {}, your account balance is : ${}'.format(usr_name, cur_bal))
    while True:
        amt = float(input('Enter the amount to be withdrawed in your account : '))
        if cur_bal > amt:
            total_bal = float(cur_bal) - amt
            amt_cell.value = float(total_bal)
            acc_open.save('account\{}.xlsx'.format(acc_no))
            print(
                'Hey {}, your current account balance was ${},\nand  ${} are withdrawed from your account,\nYour updated '
                'balance is ${}'.format(usr_name, cur_bal, amt, total_bal))
            stat_writer.statement_writer(acc_no, cur_bal, amt, total_bal, 3)
            break
        elif cur_bal == amt:
            print('You cannot withdraw complete amount.')
        else:
            print('You do not have sufficient amount in your account')
