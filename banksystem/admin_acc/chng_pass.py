import json

def chng_pass(admin_usr):
    admin_json = open('account\\admin.json', 'r')
    admin_data = json.load(admin_json)
    admin_json.close()
    admin_json = open('account\\admin.json', 'w')
    new_pswd = input('Enter New Admin Password: ')
    for myAdmin in admin_data['admin_list']:
        if myAdmin['admin_usr']==admin_usr:
            myAdmin['admin_pswd']=new_pswd
            print('Password Successfully Updated')
        else:
            continue
    json.dump(admin_data,admin_json)
    admin_json.close()