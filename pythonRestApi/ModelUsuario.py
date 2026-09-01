from ConexionBasededatos import ConexionMysql

class ModelUsuarios:
    def __init__(self):
        self.mibasededatos = ConexionMysql()
        self.connexion = self.mibasededatos.conexion
        self.cursor = self.mibasededatos.cursor

    def obtener_conexion(self):
        return self.mibasededatos
    
    def obtener_usuario(self, id):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def obtener_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    def insertar_usuario(self, nombre, email, contrasena):
        val = (nombre, email, contrasena)
        sql = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, val)
        self.connexion.commit()

    def actualizar_usuario(self, id, nombre, email, contrasena):
        val = (nombre, email, contrasena, id)
        sql = "UPDATE usuarios SET nombre = %s, email = %s, contrasena = %s WHERE id = %s"
        self.cursor.execute(sql, val)
        self.connexion.commit()

    def eliminar_usuario(self, id):
        val = (id,)
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, val)
        self.connexion.commit()
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.connexion.close()
    
    def verficarUsuario(self, email, password):
        val = (email, password)
        sql = "SELECT email, contrasena FROM usuarios WHERE email = %s AND contrasena = %s"
        self.cursor.execute(sql, val)

        user = self.cursor.fetchone()
        if user:
            return "index"
        else:
            return "CONTRASEÑA INCORRECTA"


