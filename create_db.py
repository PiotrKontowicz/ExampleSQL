import mysql.connector

db_name = 'test_app'
table_name = 'data'

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='P@ssw0rd'
)

mycursor = db.cursor()
mycursor.execute('DROP DATABASE IF EXISTS {}'.format(db_name))
mycursor.execute('CREATE DATABASE {}'.format(db_name))
mycursor.execute('USE {}'.format(db_name))
mycursor.execute('CREATE TABLE {} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(40), temperature INT)'.format(table_name))
mycursor.execute('CREATE TABLE admins (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))')
mycursor.execute('INSERT INTO admins (id, name) VALUES (1, \'test_admin\')'.format(table_name))
mycursor.execute('INSERT INTO {} (id, name, temperature) VALUES (1, \'Bathroom\', 0)'.format(table_name))
mycursor.execute('INSERT INTO {} (id, name, temperature) VALUES (2, \'Kitchen\', 0)'.format(table_name))
db.commit()