
from flask import Flask, render_template, request, render_template_string
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'P@ssw0rd'
mysql = MySQL(app)

safe = True

@app.route('/name')
def view_selected():
    name = request.args['name']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('USE test_app')
    try:
        if safe == False:
            query = 'SELECT * FROM data where name=\'{}\''.format(name)
            print(query)
            cursor.execute(query)        
            data = list(cursor.fetchall())
            return render_template('table.html', data = data)
        if safe == True:
            cursor.execute('SELECT * FROM data where name=%s', (name,))
            print(name)
            data = list(cursor.fetchall())
            return render_template('table.html', data = data)
    except Exception as e:
        return str(e)

@app.route('/')
def view_all():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('USE test_app')
    cursor.execute('SELECT * FROM data')
    data = list(cursor.fetchall())
    
    return render_template('table.html', data = data)

@app.route('/save')
def save_data():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('USE test_app')
    try:
        if safe == False:
            query = 'INSERT INTO data (name, temperature) VALUES (\'{}\', {})'.format(request.args['name'], request.args['temperature'])
            print('Query: {}'.format(query))
            cursor.execute(query)
            mysql.connection.commit()
            return 'ok'
        if safe == True:
            cursor.execute('INSERT INTO data (name, temperature) VALUES (%s, %s)', (request.args['name'], request.args['temperature'],))
            mysql.connection.commit()
            return 'ok'
    except Exception as e:
        return str(e)

if __name__ == '__main__': 
    app.run()