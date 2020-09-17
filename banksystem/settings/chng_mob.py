import json

def mobile_change(acc_no):
    acc_json = open('account\{}.json'.format(acc_no),'r')
    acc_data = json.load(acc_json)
    usr_name = acc_data['fname']
    prev_mob = acc_data['mobile']
    acc_json.close()
    print('Hey {}, Your Current Mobile No. is : {}'.format(usr_name, prev_mob))
    
    mob_ch = 0
    while mob_ch!=1:
        print('Enter New Mobile No. ')
        new_mob = input('>> ')
        if len(new_mob)==10:
            mob_ch=1
        else:
            print('Invalid Mobile No.')
            continue
    acc_json = open('account\{}.json'.format(acc_no),'w')
    acc_data['mobile'] = new_mob
    json.dump(acc_data,acc_json)
    acc_json.close()
    print('Hey {}, Your Mobile No. is successfully updated.'.format(usr_name))