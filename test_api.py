import requests

# Yeh features tu apne model ke liye bhej raha hai.
# Features ko apne model ke according update kar.
# These features are hypothetical and will need to be adjusted based on your model's training.
features = [0.8, 1.5, 3.9, 1.1, 2.0, 1.3, 0.9, 0.6, 0.5, 1.9, 0.8]


# Flask server pe POST request bhejna
response = requests.post("http://127.0.0.1:5005/predict", json={"features": features})

# Result print karna
print(response.json())  # Yeh output jo return karega
