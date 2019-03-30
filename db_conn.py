from flask_mysqldb import MySQL

class DBConn:
    def __init__(self, app):
        #self.host = host
        #self.usuario = usuario
        #self.password = password
        #self.database = database
       
       

    def conectar(self):
        #""" Crear una conexion con la base de datos """
        self.mysql =  MySQL(self.app)
        #self.db = MySQL.connect(host=self.host, user=self.usuario, passwd=self.password, db=self.database)
    
    def abrir_cursor(self):
        #""" Abrir un cursor""""
        self.cursor = self.mysql.connection.cursor() 
         

    def ejecutar_consulta(self, query, valores=''):
        #""" Ejecutar una consulta en la BD""""
        if valores != '':
            self.cursor.execute(query, valores)
        else:
            self.cursor.execute(query)
    
    def traer_datos(self):
        #""" Traer todos los registros de la consulta"""
        self.rows = self.cursor.fetchall
    
    def send_commit(self, query):
        #""" Enviar Commit a la base de datos """
        sql = query.lower()
        es_select = sql.count('select')
        if es_select < 1:
            self.db.commit()

    def cerrar_cursor(self):
        #""" Cerrar cursor"""
        self.cursor.close()

    def ejecutar(self, query, valores=''):
        if (self.host and self.usuario and self.password and self.database and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query, valores)
            self.traer_datos()
            self.cerrar_cursor()

            return self.rows
    