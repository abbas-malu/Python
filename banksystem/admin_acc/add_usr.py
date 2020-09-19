import json

def add_usr():
    admin_json = open('account\\admin.json', 'r')
    admin_data = json.load(admin_json)
    admin_json.close()
    admin_json = open('account\\admin.json', 'w')
    new_admin_name = input('Enter New Admin Username: ')
    new_admin_pswd = input('Enter New Admin Password: ')
    admin_data['admin_list'].append({"admin_usr": new_admin_name,"admin_pswd": new_admin_pswd})
    json.dump(admin_data,admin_json)
    admin_json.close()