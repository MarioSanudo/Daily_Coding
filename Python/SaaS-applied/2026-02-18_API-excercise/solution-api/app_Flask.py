from flask import Flask, request
from flask_restful import Api, Resource
from biomechanics import calculate_saddle_height

app=Flask(__name__)
api=Api(app)

@app.route("/api/health", methods=["GET"])
def check_api():
    return {"status": "ok", "service": "boimechanics-api"}

@app.route("/api/saddle-height", methods=["POST"])
def saddle_height():
    biomechanical_dic=request.get_json()
    print(biomechanical_dic)    #Lo lee
    
    try:
            
        if biomechanical_dic:
            bio_dic=calculate_saddle_height(biomechanical_dic["inseam_cm" ], biomechanical_dic["method"])
            return bio_dic, 200

    except ValueError:
        return "Ha ocurrido un error con el formato, o su longitud no es correcta", 422
    
    else:
        return "No has introducido los campos necesarios", 400
    

if __name__ == "__main__":
    app.run(debug=True)






