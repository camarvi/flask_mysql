from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_mysqldb import MySQL
from class_contacto import Contacto

app = Flask(__name__)

# Conexion a la base de datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='servidor'
app.config['MYSQL_DB']='flaskcontact'

#mysql =  MySQL(app)

#Configuraciones
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    contactos = Contacto()  
    lista_contactos = contactos.leer_contactos()  
    #cur = mysql.connection.cursor()    
    #cur.execute('SELECT * FROM contacts')
    #data = cur.fetchall()
    return render_template('index.html', contacts = lista_contactos)


# nuevo contacto
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


# Modificar un contacto
@app.route('/edit/<id>')
def get_contact(id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts WHERE id= %s', (id))
        data = cur.fetchall()
        return render_template('edit-contact.html', contact = data[0])

# Actualiza contacto
@app.route('/update/<id>', methods=['POST'])   
def update_contact(id):
         if request.method == 'POST':
                fullname = request.form['fullname']
                phone = request.form['phone']
                email = request.form['email']
                cur = mysql.connection.cursor()
                cur.execute("""
                UPDATE contacts 
                SET fullname = %s,
                        phone = %s,
                        email = %s
                 WHERE id = %s     
                """, (fullname, phone, email, id))
                mysql.connection.commit()
                flash('Contacto Actualizado')
                return redirect(url_for('index'))

# Eliminar un contacto
@app.route('/delete/<string:id>')
def delete_contact(id):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM contacts WHERE id= {0}'.format(id))   
        mysql.connection.commit() 
        flash('Contacto Eliminado')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)