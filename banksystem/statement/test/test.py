import json
import requests
with open('test.json', 'r') as js:
    data = json.load(js)

acc_name = data['fname']
acc_pass = data['acc_pswd']
print(acc_name,acc_pass)
for date in data['statement']:
    print("date: {} withdraw: {} deposit: {}".format(date['date'],date['dr'],date['cr']))
data['balance'] = 21231112321
with open('test.json', 'w') as js:
    json.dump(data,js)

# data = requests.get('https://api.edamam.com/search?q=chicken&app_id=b1abbd20&app_key=ed8615224941901e13da0800b5d222af')
# print(data.content)
# recipe = json.loads(data.content)
# for x in recipe['hits']:
#     print(x)
