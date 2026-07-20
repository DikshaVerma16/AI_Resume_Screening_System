from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# Create Flask App
app = Flask(__name__)
CORS(app)

# Load ML files
model = joblib.load("resume_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
encoder = joblib.load("label_encoder.pkl")

# Home Page
@app.route("/")
def home():
    return "AI Resume Screening System is Running!"

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    resume = data["resume"]

    resume_vector = vectorizer.transform([resume])

    prediction = model.predict(resume_vector)

    category = encoder.inverse_transform(prediction)

    return jsonify({
        "prediction": category[0]
    })


if __name__ == "__main__":
    app.run(debug=True)