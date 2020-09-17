import json


def name_change(acc_no):
    acc_json = open('account\{}.json'.format(acc_no),'r')
    acc_data = json.load(acc_json)
    usr_name = acc_data['fname']
    acc_json.close()
    print('Hey {}, Your Current User name is : {}'.format(usr_name,usr_name))
    print('Enter New Username ')
    new_name = input('>> ')
    acc_json = open('account\{}.json'.format(acc_no),'w')
    acc_data['fname'] = new_name 
    json.dump(acc_data,acc_json)
    acc_json.close()
    print('Hey {}, Your username is successfully updated.'.format(usr_name))