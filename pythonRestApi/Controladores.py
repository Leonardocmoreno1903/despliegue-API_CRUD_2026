from ModelUsuario import ModelUsuarios
#from flask_login import LoginManager
from flask import Flask, jsonify, request
from flask_cors import CORS
#la linea 6 y 7 se borran para subir el archivo a github
#app = Flask(__name__)
#app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave-local')

CORS(app)
usuarios = ModelUsuarios() 


@app.route('/login', methods=['POST'])
def loginUsuario():
    email = request.json['email']
    password = request.json['password']
    resultado = usuarios.verficarUsuario(email, password)
    return jsonify({"mensaje": resultado})

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios.obtener_usuarios())

@app.route('/usuario/<int:id>', methods=['GET'])
def listar_usuario(id):
    return jsonify(usuarios.obtener_usuario(id))

@app.route('/nuevo_usuario', methods=['POST'])
def crear_usuario():
    nombre = request.json['nombre']
    email = request.json['email']
    contrasena = request.json['contrasena']
    usuarios.insertar_usuario(nombre, email, contrasena)
    return jsonify({"mensaje": "USUARIO CREADO EXITOSAMENTE"})

@app.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    contrasena = data.get('contrasena')
    if nombre is None and email is None and contrasena is None:
        return jsonify({"error": "NO SE PRORPORCIONARON DATOS PARA ACTUALIZAR"}), 400
    
    usuario_existente = usuarios.obtener_usuario(id)    
    if usuario_existente:
        usuarios.actualizar_usuario(id, nombre, email, contrasena)
        return jsonify({"mensaje": "USUARIO ACTUALIZADO CORRECTAMENTE"})
    else:
        return jsonify({"error": "EL USUARIO NO EXISTE"}), 404

@app.route('/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if usuarios.obtener_usuario(id):
        usuarios.eliminar_usuario(id)
        return jsonify({"mensaje": "USUARIOS ELIMINADO CORRECTAMENTE"})
    else:
        return jsonify({"error": "EL USUARIO NO EXISTE"}), 404



#para hacer el despligue modifico esta linea y paso el valor TRUE POR FALSE
if __name__ == '__main__':
    app.run(debug=False)

