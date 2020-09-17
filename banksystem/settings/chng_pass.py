import json


def password_change(acc_no):
    acc_json = open('account\{}.json'.format(acc_no),'r')
    acc_data = json.load(acc_json)
    usr_name = acc_data['fname']
    prev_pass = acc_data['pswd']
    acc_json.close()
    print('Hey {}, Enter Your Current Password :'.format(usr_name))
    curr_pass = input('>> ')
    while curr_pass != prev_pass:
        print('Wrong Password. Try Again')
        curr_pass = input('>> ')
    else:
        print('Enter New Password')
        new_pass = input('>> ')
        acc_json = open('account\{}.json'.format(acc_no),'w')
        acc_data['pswd'] = new_pass
        json.dump(acc_data,acc_json)
        acc_json.close()
    print('Hey {}, Your password is successfully updated.'.format(usr_name))
