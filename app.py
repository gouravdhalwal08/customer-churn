from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('churn_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # Make sure input is a list of numbers (length = number of features)
    try:
        input_features = np.array(data['features']).reshape(1, -1)
    except:
        return jsonify({"error": "Invalid input format. Must be a list of numbers."})

    # Make prediction
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0][1]

    return jsonify({
        'prediction': int(prediction),
        'churn_probability': float(probability)
    })

if __name__ == '__main__':
    app.run(debug=True,port=5005)
