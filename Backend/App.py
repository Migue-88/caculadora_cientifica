# API que recibe operaciones y devuelve resultados
from flask import Flask, request, jsonify
from flask_cors import CORS
import math
#Crea la aplicacion Flask
app = Flask(__name__)
CORS(app) # Permite enviar solicitudes desde cualquier origen

#Definimos ruta para enviar solicitudes POST
@app.route('/calcular', methods=['POST'])
def calcular ():
    #Obtener datos enviados en formato JSON
    data = request.get_json()

    #Extrae la expresión matematica enviada desde Front
    expresion = data.get ("expresion")

    try:
        #Evalua la expresión matemática
        resultado = eval(expresion)
        #Retoma el resultado en formato JSON
        return jsonify({"resultado": resultado})
    
    except Exception as e:
        #Si hay error muestra el mensaje de error
        return jsonify({"Se presento un error": str(e)}), 400
    
#Ejecuta la aplicaciónm en modo debug para pruebas
if __name__ == '__main__':
    app.run(debug=True)
