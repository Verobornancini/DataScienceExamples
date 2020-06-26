import logging

from flask import Flask, jsonify, request
from flask_swagger import swagger
from flask_cors import CORS

import joblib
import numpy as np

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
logging.getLogger('flask_cors').level = logging.DEBUG

@app.route("/predict", methods=['POST'])
def predict():
    """
    Predict salary
    ---
    tags:
      - predict
    description: 'Predict salary given years of experience'
    parameters:
      - in: body
        name: input array of years of experience
        schema:
            type: array
            items:
            type: integer
            minItems: 1
    responses:
      200:
        description: Predicted salary
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            years_of_experience = np.array(data).reshape(-1, 1)

            lin_reg = joblib.load("./linear_regression_model.pkl")
        except ValueError:
            return jsonify("Please enter a number.")

        return jsonify(lin_reg.predict(years_of_experience).tolist())


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['host'] = 'localhost:5000'
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Salary prediction API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run(debug=True)
