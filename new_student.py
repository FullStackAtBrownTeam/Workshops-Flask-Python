from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3 as sql
# create an SQLite database 'database.db' 
# and create a students' table in it

# create a connection object that represents the database
conn = sql.connect('database.db')
print ("Opened database successfully")

conn.execute('DROP TABLE students')
# execute the sql command
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created successfully")

# close the database connection
conn.close()


@app.route('/enternew')
def new_student():
    return render_template('new_student.html')

# form data is posted to '/addrec' URL which binds to addrec()
# addrec() retrieves the form data by POST method
#       and inserts in students table
@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect('database.db') as con:
                # cursor is like iterator, facilitate traversal, retrieval, addition, removal of db records
                cur = con.cursor()
                cur.execute('INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)', 
                (nm, addr, city, pin))
                # ? as placeholder for variable values

                con.commit()  # commits the current transaction to the db
                msg = 'Record successfully added'
        
        except:
            con.rollback()  # rolls back any changes to the db since last commit() call
            msg = 'error in insert operation'
        
        finally:  # execute the code regardless of the result of try/except
            return render_template('student_result.html', msg = msg)
            con.close()  # closes the db connection


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row  #provides index-based access to columns

    cur = con.cursor()
    cur.execute('SELECT * FROM students')

    rows = cur.fetchall()  #fetch all rows of the query results
    return render_template('list.html', rows = rows)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)