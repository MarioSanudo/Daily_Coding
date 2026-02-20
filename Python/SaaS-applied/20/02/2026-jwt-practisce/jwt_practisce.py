from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token
import datetime
from dotenv import load_dotenv
import os



app=Flask(__name__)
load_dotenv()
app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")

JWT= JWTManager()   #Creariamos la instancia

JWT.init_app(app)

@app.route("/", methods=["POST"])
def principal():

    usuario= request.get_json()
    if usuario is None:
        return {"Error", "La información no se ha enviado"}

    email= usuario["Email"].split()
    password= usuario["Password"]

    print(f"Email del usuario {email} y su contraseña es {password}")

    actual_time= datetime.date.today()
    print(actual_time)
    expire_time=datetime.timedelta

    token=create_access_token(usuario)

    return token



if __name__== "__main__":
    app.run(debug=True)


    

