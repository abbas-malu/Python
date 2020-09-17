import json


def chk_bal(act_number):
    acc_json = open('account\{}.json'.format(act_number),'r')
    acc_data = json.load(acc_json)
    cur_bal = acc_data['balance']
    usr_name = acc_data['fname']
    print('Hey {}, your current account balance is ${}'.format(usr_name,cur_bal))
    acc_json.close()
