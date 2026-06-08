# Malicious URL Detection System

## Overview

The Malicious URL Detection System is a machine learning project that analyzes website URLs and predicts whether they are legitimate or potentially malicious. The system uses URL-based feature extraction and a Random Forest classifier to identify suspicious patterns commonly found in phishing, malware, and defacement URLs.

A Streamlit web application is provided to perform real-time URL analysis through a simple and interactive user interface.

---

## Features

* Real-time URL classification
* URL feature extraction and analysis
* Machine Learning based prediction
* Confidence score generation
* Interactive Streamlit web application
* Binary classification:

  * Legitimate (Benign)
  * Malicious

---

## Dataset

The model was trained using a large URL dataset containing over 650,000 labeled URLs belonging to categories such as:

* Benign
* Phishing
* Malware
* Defacement

For training purposes, all malicious categories were combined into a single "Malicious" class.

---

## Feature Engineering

The system extracts multiple URL-based features, including:

* URL Length
* Domain Length
* Path Length
* Number of Dots
* Number of Hyphens
* Number of Digits
* Number of Slashes
* Number of Query Parameters
* Presence of IP Address
* Presence of Suspicious Keywords
* Special Character Counts

These features are converted into numerical values and used as input for the machine learning model.

---

## Machine Learning Model

### Random Forest Classifier

The project uses a Random Forest Classifier to learn patterns from URL structures and classify URLs as legitimate or malicious.

Model Evaluation Results:

* Accuracy: 87%+
* Precision: High
* Recall: High
* F1 Score: Balanced Performance

---

## Project Structure

```text
Malicious URL Detection System
│
├── app.py
├── train_model.py
├── feature_extraction.py
├── requirements.txt
│
├── dataset/
│   └── malicious_phish.csv
│
└── model/
    └── phishing_model.pkl
```

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib
* URL Parsing Utilities

---

## Application Workflow

1. User enters a URL.
2. The system extracts URL features.
3. Features are converted into numerical values.
4. The trained Random Forest model analyzes the features.
5. The model predicts whether the URL is legitimate or malicious.
6. The result and confidence score are displayed to the user.

---

## Example Analysis

Input URL:

```text
secure-login-bank-verification.xyz
```

Output:

```text
Prediction: Malicious URL
Confidence Score: 94%
```

---

## Future Improvements

* Domain reputation analysis
* WHOIS information integration
* SSL certificate validation
* DNS feature extraction
* Deep Learning based URL classification
* Browser extension deployment

---

## Author

Ahmed Amir

Machine Learning | Python Development | Data Science
