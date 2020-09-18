import mysql.connector

mydb = mysql.connector.connect(host='localhost',username='root',password='')


cur = mydb.cursor()

cur.execute('SELECT * FROM `students`.`p_details`')

results = cur.fetchall()

# for target_list in results:
#     print(target_list)
# print(results)

for i in range(1,100000):
    qry = "insert into `students`.`p_details` (name, age, gender, email, phone, class, section) values ('{}', {}, 'Male', '{}', '{}', {}, '{}');".format('student'+str(i),25,'abcpqr'+str(i)+'@xyz.com','6232705352','12','A')
    cur.execute(qry)

mydb.commit()