import xlrd
import openpyxl


def mobile_change(acc_no):
    mob_acc = xlrd.open_workbook('account\{}.xlsx'.format(acc_no))
    mob_sheet = mob_acc.sheet_by_name('maindata')
    usr_name = mob_sheet.cell_value(0, 0)
    acc_open = openpyxl.load_workbook('account\{}.xlsx'.format(acc_no))
    worksheet = acc_open['maindata']
    prev_mob1 = '+91'+str(int(mob_sheet.cell_value(1, 0)))
    prev_mob2 = worksheet.cell(1, 1)
    print('Hey {}, Your Current Mobile No. is : {}'.format(usr_name, prev_mob1))
    print('Enter New Mobile No. ')
    new_mob = input('>> ')
    prev_mob2.value = new_mob
    acc_open.save('account\{}.xlsx'.format(acc_no))
    print('Hey {}, Your Mobile No. is successfully updated.'.format(usr_name))