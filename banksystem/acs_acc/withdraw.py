import json
from statement import stat_writer


def withdraw(acc_no):
    acc_json = open('account\{}.json'.format(acc_no), 'r')
    acc_data = json.load(acc_json)
    usr_name = acc_data['fname']
    cur_bal = float(acc_data['balance'])
    print('Hey {}, your account balance is : ${}'.format(usr_name, cur_bal))
    acc_json.close()
    while True:
        amt = float(input('Enter the amount to be withdrawed in your account : '))
        if (cur_bal > amt) & (cur_bal!=0) & (amt>0):
            total_bal = float(cur_bal) - amt
            acc_json = open('account\{}.json'.format(acc_no), 'w')
            acc_data['balance'] = float(total_bal)
            json.dump(acc_data, acc_json)
            acc_json.close()
            print(
                'Hey {}, your current account balance was ${},\nand  ${} are withdrawed from your account,\nYour updated '
                'balance is ${}'.format(usr_name, cur_bal, amt, total_bal))
            stat_writer.statement_writer(acc_no, cur_bal, amt, total_bal, 2)
            break
        elif cur_bal == amt:
            print('You cannot withdraw complete amount.')
        else:
            print('You do not have sufficient amount in your account or invalid amount entered')
            break
