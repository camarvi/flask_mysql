from db_conn import DBConn

class Contacto:
    def __init__(self):
        self.id = 0
        self.fullname = ""
        self.phone = ""
        self.mail = ""
        self.db = DBConn()

    def nuevo_contacto(self):
        query = 'INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)'
        valores = (self.fullname, self.phone, self.email))
        self.db.ejecutar(query, valores)
    
    def elimina_contacto(self):
        query = 'DELETE FROM contacts WHERE id= %s'
        valores = (self.id)
        self.db.ejecutar(query, valores)

    def modifica_contacto(self):
        query = 'UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s'
        valores = (self.fullname, self.phone, self.mail, self.id)
        self.db.ejecutar(query, valores)

    def leer_contactos(self):
        query = 'SELECT * FROM contacts'
        self.db.ejecutar(query)

    def leer_contacto(self):
        query = 'SELECT * FROM contacts WHERE id= %s'
        valores = (self.id)
        self.db.ejecutar(query, valores)        