import mysql.connector
import time
import random

db_name = 'test_app'
table_name = 'data'

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='P@ssw0rd'
)

mycursor = db.cursor()

mycursor.execute('USE {}'.format(db_name))
cnt = 0
while True:

    mycursor.execute('UPDATE data set temperature = {} where id=1'.format(random.randint(-20,50)))
    mycursor.execute('UPDATE data set temperature = {} where id=2'.format(random.randint(-20,50)))
    db.commit()
    time.sleep(10)
