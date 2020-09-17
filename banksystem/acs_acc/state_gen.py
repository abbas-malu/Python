import json
from tabulate import tabulate

def stat_gen(acc_no):
    acc_json = open('account\{}.json'.format(acc_no), 'r')
    acc_data = json.load(acc_json)
    amt_list = []
    for stat in acc_data['statement']:
        amt_list.append([stat['date'],stat['dr'],stat['cr'],stat['up_bal']])
    print(tabulate(amt_list, headers=['Date', 'Withdraw','Deposit','Balance']))
    acc_json.close()
