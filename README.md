# AI-Powered Resume Screening and Job Category Prediction System

## Project Overview

The AI-Powered Resume Screening and Job Category Prediction System is a web-based application that automatically classifies resumes into different job categories using Machine Learning and Natural Language Processing (NLP).

The system reduces the manual effort required in resume screening by predicting the most suitable job category based on the resume text entered by the user.

---

## Features

- Automatic resume category prediction
- Natural Language Processing (NLP)
- TF-IDF text vectorization
- LinearSVC Machine Learning model
- Flask backend API
- Interactive web interface using HTML, CSS, and JavaScript
- Fast and accurate predictions

---

## Technologies Used

### Programming Language
- Python

### Machine Learning Libraries
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend
- Flask
- Flask-CORS

### Frontend
- HTML
- CSS
- JavaScript

### Development Tools
- Google Colab
- Visual Studio Code

---

## Dataset

**Source:** Kaggle Resume Dataset

**Dataset Details:**
- Total Resumes: 2484
- Features:
  - ID
  - Resume_str
  - Resume_html
  - Category

The `Resume_str` column is used as input for training, while the `Category` column is used as the target label.

---

## Project Structure

```
AI_Resume_Screening_System/
│
├── backend/
│   ├── app.py
│   ├── resume_classifier.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
├── report/
├── ppt/
├── README.md
└── requirements.txt
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Resume_Screening_System.git
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Backend

```bash
cd backend
py app.py
```

The Flask server will start at:

```
http://127.0.0.1:5000
```

### Step 4: Run the Frontend

Open the `frontend` folder in Visual Studio Code and start **Live Server**.

---

## API Documentation

### Endpoint

```
POST /predict
```

### Request

```json
{
  "resume": "Paste your resume text here"
}
```

### Response

```json
{
  "prediction": "HR"
}
```

---

## Workflow

1. User enters resume text.
2. Frontend sends the text to the Flask API.
3. The backend preprocesses the text.
4. TF-IDF converts the text into numerical features.
5. LinearSVC predicts the job category.
6. The predicted category is displayed on the webpage.

---

## Advantages

- Fast resume classification
- Reduces manual screening effort
- Easy-to-use interface
- Machine Learning-based prediction
- Scalable web application

---

## Future Scope

- Upload PDF and DOCX resumes
- Resume ranking based on job descriptions
- Skill extraction
- Candidate recommendation
- Cloud deployment
- Multilingual resume support

---

## Author

**Diksha Verma**

**Roll No.:** 202401100800074

**Branch:** Information Technology (IT)

**Semester:** 5th

**College:** KIET Group of Institutions, Ghaziabad

---

## License

This project is developed for educational purposes as part of the B.Tech Information Technology curriculum at KIET Group of Institutions.