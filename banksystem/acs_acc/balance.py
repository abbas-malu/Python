import xlrd


def chk_bal(act_number):
    bl_acc = xlrd.open_workbook('account\{}.xlsx'.format(act_number))
    bl_sheet = bl_acc.sheet_by_name('maindata')
    cur_bal = float(bl_sheet.cell_value(3,0))
    usr_name = bl_sheet.cell_value(0,0)
    print('Hey {}, your current account balance is ${}'.format(usr_name,cur_bal))
