import json
from tabulate import tabulate

def view_acc():
    admin_json = open('account\\admin.json', 'r')
    admin_data = json.load(admin_json)
    acc_in_bank = admin_data['accounts']
    admin_json.close()
    acc_list = []
    for account in acc_in_bank:
        acc_list.append([acc_in_bank.index(account)+1 ,account['acc_no'],account['acc_holder'],account['mobile'],account['d_o_c']])
    print(tabulate(acc_list, headers=['S No.','Account No.','Account Holder','Mobile No.','Date']))
