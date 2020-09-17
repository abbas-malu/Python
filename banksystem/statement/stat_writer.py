import json
from statement import get_date


def statement_writer(acc_no, prev_bal, add_with, up_bal, type_transaction):
    date = get_date.date_today()
    acc_json = open('account\{}.json'.format(acc_no), 'r')
    acc_data = json.load(acc_json)
    acc_json.close()
    acc_json = open('account\{}.json'.format(acc_no), 'w')
    if type_transaction == 1:
        cur_stat = {'date': date, 'cr':add_with, 'dr': 0.0}
    else:
        cur_stat = {'date': date, 'cr':0.0, 'dr': add_with}
    acc_data['statement'].append(cur_stat)
    json.dump(acc_data,acc_json)