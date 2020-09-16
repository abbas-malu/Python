import random
import xlsxwriter
from statement import get_date


def create_acc():
    date = get_date.date_today()
    first_name = input("Enter Account Holder First Name : ").lower()
    last_name = input("Enter Account Holder Last Name : ").lower()
    father_name = input("Enter Account Holder Father's Name : ").lower()
    ad_ch = 0
    while ad_ch != 1:
        aadhar_no = int(input("Enter Account Holder Aadhar Card Number : "))
        if len(str(aadhar_no)) == 12:
            ad_ch = 1
        else:
            print('Enter Valid Aadhar Number')
            continue
    mo_ch = 0
    while ad_ch != 1:
        mob_no = int(input("Enter Mobile No. For Registration As (9988776655) : "))
        if len(str(mob_no)) == 10:
            mo_ch = 1
        else:
            print('Enter Valid Mobile Number')
            continue
    acc_no = 'py' + str(random.randrange(1000, 9999))
    pswd_def = first_name[:2] + acc_no
    acc_open = xlsxwriter.Workbook('account\{}.xlsx'.format(acc_no))
    worksheet = acc_open.add_worksheet('maindata')
    statement_work = acc_open.add_worksheet('statement')
    rec_keep = acc_open.add_worksheet('record')
    pswd_usr = input('Enter Password To be Used For Your Account\n(Leave Blank to use default password)\n>>')
    if pswd_usr == '':
        pswd = pswd_def
    else:
        pswd = pswd_usr
    worksheet.write(0, 0, first_name)
    worksheet.write(0, 1, last_name)
    worksheet.write(0, 2, father_name)
    worksheet.write(0, 3, aadhar_no)
    worksheet.write(1, 0, mob_no)
    worksheet.write(2, 0, pswd)
    worksheet.write(3, 0, 0.0)
    rec_keep.write(0, 0, 3)
    statement_work.write(0, 0, 'Date')
    statement_work.write(1, 0, date)
    statement_work.write(0, 1, 'Credit')
    statement_work.write(0, 2, 'Debit')
    statement_work.write(0, 3, 'Balance')
    statement_work.write(1, 3, 0)
    print('''Your Account Is Successfully Created.
Your Account Number is          : {} 
Account Holder Name is          : {} {}
Your Registered Mobile No. Is   : {}
Your Aadhaar Number is          : {}
Password To Access Your Account : {}
Your Current Account Balance is : {}'''.format(acc_no, first_name, last_name, mob_no, aadhar_no, pswd, '$0'))
    acc_open.close()
