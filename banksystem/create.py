import random
import json
import os
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
    while mo_ch != 1:
        mob_no = int(input("Enter Mobile No. For Registration As (9988776655) : "))
        if len(str(mob_no)) == 10:
            mo_ch = 1
        else:
            print('Enter Valid Mobile Number')
            continue
    acc_no = 'py' + str(random.randrange(1000, 9999))
    acc_ex_chk = 0
    while acc_ex_chk !=1:
        if os.path.exists('account\{}.json'.format(acc_no)):
            acc_no = 'py' + str(random.randrange(1000, 9999))
        else:
            acc_ex_chk = 1
    pswd_def = first_name[:2] + acc_no
    acc_json = open('account\{}.json'.format(acc_no),'w')
    pswd_usr = input('Enter Password To be Used For Your Account\n(Leave Blank to use default password)\n>>')
    if pswd_usr == '':
        pswd = pswd_def
    else:
        pswd = pswd_usr
    acc_js_write = {'fname': first_name, 'lname': last_name, 'father_name': father_name, 'dhaar': aadhar_no, 'mobile': mob_no,
                    'balance': 0.0, 'pswd': pswd, 'date_created':get_date.date_today(), 'statement':[]}
    json.dump(acc_js_write,acc_json)
    print('''Your Account Is Successfully Created.
Your Account Number is          : {} 
Account Holder Name is          : {} {}
Your Registered Mobile No. Is   : {}
Your Aadhaar Number is          : {}
Password To Access Your Account : {}
Your Current Account Balance is : {}'''.format(acc_no, first_name, last_name, mob_no, aadhar_no, pswd, '$0.0'))
    acc_json.close()
    admin_json = open('account\\admin.json','r')
    admin_data = json.load(admin_json)
    admin_json.close()
    admin_json = open('account\\admin.json', 'w')
    admin_data['accounts'].append({'acc_no':acc_no,'acc_holder': "{} {}".format(first_name, last_name),'mobile':mob_no, "d_o_c":date})
    json.dump(admin_data,admin_json)
    admin_json.close()
