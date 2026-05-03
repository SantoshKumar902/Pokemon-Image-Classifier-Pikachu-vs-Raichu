from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import io

app = Flask(__name__)
CORS(app)

model = load_model('pokemon_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    img = image.load_img(io.BytesIO(file.read()), target_size=(64, 64))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    result = model.predict(img_array)
    confidence = float(result[0][0])
    
    if confidence >= 0.5:
        prediction = "Pikachu"
    else:
        prediction = "Raichu"
        confidence = 1 - confidence
    
    return jsonify({"prediction": prediction, "confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)