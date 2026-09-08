""" import os
import mysql.connector
from mysql.connector import Error


class ConexionMysql:

    def __init__(self):
        try:

            self.mibasededatos = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                port=os.getenv("DB_PORT", "3306"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=os.getenv("DB_NAME", "prueba")
            )

            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()

            if self.mibasededatos.is_connected():

                db_Info = self.mibasededatos.get_server_info()

                print(
                    f"CONECTADO A MYSQL SERVER, VERSION: {db_Info}"
                )

        except Error as e:

            print(f"Error al conectar con MySQL: {e}")


    def cerrar_conexion(self):

        if self.mibasededatos.is_connected():

            self.cursor.close()
            self.conexion.close()

            print("CONEXION CERRADA CORRECTAMENTE")


if __name__ == "__main__":

    conexion = ConexionMysql()
    conexion.cerrar_conexion() """

import os
import mysql.connector
from mysql.connector import Error


class ConexionMysql:

    def __init__(self):
        try:
            self.mibasededatos = mysql.connector.connect(
                host=os.getenv("MYSQLHOST"),
                port=int(os.getenv("MYSQLPORT", "3306")),
                user=os.getenv("MYSQLUSER"),
                password=os.getenv("MYSQLPASSWORD"),
                database=os.getenv("MYSQL_DATABASE")
            )

            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()

            if self.mibasededatos.is_connected():
                db_info = self.mibasededatos.get_server_info()

                print(
                    f"CONECTADO A MYSQL SERVER, VERSION: {db_info}"
                )

        except Error as error:
            print("Error al conectar con MySQL:", error)