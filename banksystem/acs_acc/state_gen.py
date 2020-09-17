import json


def stat_gen(acc_no):
    acc_json = open('account\{}.json'.format(acc_no), 'r')
    acc_data = json.load(acc_json)
    for stat in acc_data['statement']:
        print("Date: {} Deposit: {} Withdraw: {} Balance: {}".format(stat['date'],stat['cr'],stat['cr'],stat['cr']))