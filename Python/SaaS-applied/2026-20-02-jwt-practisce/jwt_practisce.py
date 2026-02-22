from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
import datetime
from dotenv import load_dotenv
from jwt_db_revoke import User, Jwt_Revoque, db
from pathlib import Path
import os

folder=Path(__file__).resolve().parent
db_route=folder / "database.db"

class Person:
    _user=[]

    def __init__(self, email_input, password_input):
        self.email=email_input
        self.password=password_input


    @classmethod
    def found_user(cls, email):
        for usuario in cls._user:
            if usuario.email == email:
                return usuario
        return None

    


app=Flask(__name__)
JWT= JWTManager() #Creariamos la instancia

load_dotenv()
app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///" + db_route.as_posix()
app.config["TRACK_MODIFICATIONS"]=False

#Después de configurar
db.init_app(app)
JWT.init_app(app)   #Inicializamos como siempre sin hardcoding

@app.route("/login", methods=["POST"])
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

    user=Person(email, password)
    Person._user.append(user)

    print(f"Email del usuario {email} y su contraseña es {password}")

    current_time=datetime.datetime.now()
    additional_time= current_time + datetime.timedelta(minutes=10)

    expire_time=additional_time - current_time
    print(expire_time)

    additional_info={"Aficiones": "Ciclismo", "Edad": 20}

    db.session.add(User(email=email))
    db.session.commit()
    
    token=create_access_token(email, expires_delta= expire_time, additional_claims=additional_info)


    return token



@app.route("/check_token", methods=["GET"])  #Vamos a leer el token no voy a crear nada
@jwt_required()   
def check_token():
    email=get_jwt_identity()
    print(email)
    return jsonify({email: "Token Válido"})



@app.route("/additional_params", methods=["GET"])
@jwt_required()
def getting_additional_params():
    print(Person._user)
    return get_jwt()        #Devolvemos toda la info del json y además del claim que hemos añadido


@app.route("/logout", methods=["DELETE"])   #Por convenio hay que ponerlo así, más legibilidad
@jwt_required()
def logout():
    email=get_jwt_identity()
    jti=get_jwt()["jti"]

    #user=Person.found_user(email)        Teniendo el token, no tiene sentido es mucho peor así, pero la opción existe aunque da falla con el debugger
    #print(user.email)       

    user_id=db.session.query(User).filter_by(email=email).first()

    revoked=Jwt_Revoque(jti=jti, user_id=user_id.id)
    db.session.add(revoked)
    db.session.commit()

    return jsonify(msg="Token revocked")
    


if __name__== "__main__":
    with app.app_context(): #Lo creo de esta forma porque es prueba y no quiero andar con migraciones
        db.create_all()

    app.run(debug=True) #Con debug=True, pierdo los elementos en memoria de la clase


    

