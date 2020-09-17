from statement import stat_writer
import json


def add(acc_no):
    acc_json = open('account\{}.json'.format(acc_no), 'r')
    acc_data = json.load(acc_json)
    usr_name = acc_data['fname']
    cur_bal = float(acc_data['balance'])
    amt = float(input('Enter the amount to be added in your account : '))
    total_bal = float(amt) + float(cur_bal)
    acc_data['balance'] = float(total_bal)
    acc_json.close()
    acc_json = open('account\{}.json'.format(acc_no), 'w')
    json.dump(acc_data, acc_json)
    acc_json.close()
    print('Hey {}, your current account balance was ${},\nand  ${} are added to your account,\nYour updated '
          'balance is ${}'.format(usr_name, cur_bal, amt, total_bal))
    stat_writer.statement_writer(acc_no, cur_bal, amt, total_bal, 1)
