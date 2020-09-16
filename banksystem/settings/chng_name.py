import xlrd
import openpyxl


def name_change(acc_no):
    name_acc = xlrd.open_workbook('account\{}.xlsx'.format(acc_no))
    name_sheet = name_acc.sheet_by_name('maindata')
    usr_name = name_sheet.cell_value(0, 0)
    acc_open = openpyxl.load_workbook('account\{}.xlsx'.format(acc_no))
    worksheet = acc_open['maindata']
    prev_name1 = name_sheet.cell_value(0, 0)
    prev_name2 = worksheet.cell(1, 1)
    print('Hey {}, Your Current User name is : {}'.format(usr_name,usr_name))
    print('Enter New Username ')
    new_name = input('>> ')
    prev_name2.value = new_name
    acc_open.save('account\{}.xlsx'.format(acc_no))
    print('Hey {}, Your username is successfully updated.'.format(usr_name))
