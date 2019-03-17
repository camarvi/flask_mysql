from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexion a la base de datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='servidor'
app.config['MYSQL_DB']='flaskcontact'

mysql =  MySQL(app)

#Configuraciones
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    cur = mysql.connection.cursor()    
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        mysql.connection.commit()
        flash('Contacto Agregado')
        return redirect(url_for('index'))

@app.route('/edit')
def edit_contact():
    return 'edita contacto'

@app.route('/delete')
def delete_contact():
    return 'delete contacto'


if __name__ == '__main__':
    app.run(port = 3000, debug = True)