# API Documentation

## Base URL

http://127.0.0.1:5000

---

## Endpoint

### POST /predict

Predicts the job category of a resume.

### Request Body

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

### Technologies Used

- Flask
- Scikit-learn
- Joblib

### Description

The API receives resume text, converts it into TF-IDF features, predicts the job category using the trained LinearSVC model, and returns the predicted category.