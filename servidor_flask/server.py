
import joblib


from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    model = joblib.load('modelo_casas.joblib')
    
    data = request.get_json(force=True)
    predict_request = [data['metrajeconstruc'], data['metrajeterreno'], data['seguridad'], data['piscina'], data['terraza'],
       data['baños'], data['parqueo'], data['financiamiento'], data['zon_comercial'],
       data['zona_gquil - ceibos & vía a la costa'], data['zona_gquil - centro'],
       data['zona_gquil - norte'], data['zona_gquil - samborondón'], data['zona_gquil - sur'],
       data['zona_otras zonas / costa & galap.'],
       data['zona_otras zonas / sierra & oriente'], data['zona_península & ruta del sol'],
       data['zona_quito - centro&sur'], data['zona_quito - norte'],
       data['zona_quito - periférico']]
    

    prediction = model.predict([np.array(predict_request)])
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)