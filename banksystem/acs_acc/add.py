import xlrd
import openpyxl
from statement import stat_writer

def add(acc_no):

    add_acc = xlrd.open_workbook('account\{}.xlsx'.format(acc_no))
    add_sheet = add_acc.sheet_by_name('maindata')
    cur_bal = float(add_sheet.cell_value(3, 0))
    usr_name = add_sheet.cell_value(0, 0)
    acc_open = openpyxl.load_workbook('account\{}.xlsx'.format(acc_no))
    worksheet = acc_open['maindata']
    amt_cell = worksheet.cell(4,1)
    amt = float(input('Enter the amount to be added in your account : '))
    total_bal = float(amt) + float(cur_bal)
    amt_cell.value = float(total_bal)
    acc_open.save('account\{}.xlsx'.format(acc_no))
    print('Hey {}, your current account balance was ${},\nand  ${} are added to your account,\nYour updated '
          'balance is ${}'.format(usr_name, cur_bal,amt,total_bal))
    stat_writer.statement_writer(acc_no, cur_bal, amt, total_bal, 2)
