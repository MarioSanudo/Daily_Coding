from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from dotenv import load_dotenv
import os



app=Flask(__name__)
load_dotenv()
app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")


JWT= JWTManager()   #Creariamos la instancia
JWT.init_app(app)   #Inicializamos como siempre sin hardcoding

@app.route("/", methods=["POST"])
def generate_token():

    print(request.headers)  #Tienen que ir los request dentro del contexto(ruta), si no no habrá cabecera
    print(request.cookies)

    usuario= request.get_json()
    if not usuario:
        return {"Error": "No se ha enviado nada"}

    if not all(usuario.values()):
        return {"Error":"Hay valores incompletos en el usuario"} 

    email= usuario["Email"].strip()
    password= usuario["Password"]

    print(f"Email del usuario {email} y su contraseña es {password}")

    current_time=datetime.datetime.now()
    additional_time= current_time + datetime.timedelta(seconds=30)

    expire_time=additional_time - current_time
    print(expire_time)
    
    token=create_access_token(email, expires_delta= expire_time)


    return token



@app.route("/check_token", methods=["GET"])  #Vamos a leer el token no voy a crear nada
@jwt_required()   
def check_token():
    email=get_jwt_identity()
    print(email)
    return jsonify({email: "Token Válido"})
    


if __name__== "__main__":
    app.run(debug=True)


    

