import streamlit as st
import joblib

from feature_extraction import extract_features


# Load trained model
model = joblib.load("model/phishing_model.pkl")


st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🔐",
    layout="centered"
)

st.title("Phishing Website Detection")
st.write("Enter a website URL to check whether it is legitimate or phishing.")

url = st.text_input("Enter Website URL")

if st.button("Analyze URL"):
    if url == "":
        st.warning("Please enter a URL first.")

    else:
        features = extract_features(url)
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0]

        phishing_probability = probability[1] * 100
        legitimate_probability = probability[0] * 100

        if prediction == 1:
            st.error("Prediction: Phishing Website")
            st.write(f"Phishing Confidence: {phishing_probability:.2f}%")
        else:
            st.success("Prediction: Legitimate Website")
            st.write(f"Legitimate Confidence: {legitimate_probability:.2f}%")

        st.subheader("Extracted URL Features")
        st.write({
            "URL Length": features[0],
            "Domain Length": features[1],
            "Path Length": features[2],
            "Dots": features[3],
            "Hyphens": features[4],
            "@ Symbol": features[5],
            "Question Marks": features[6],
            "Equal Signs": features[7],
            "Slashes": features[8],
            "Digits": features[9],
            "HTTPS": features[10],
            "IP Address": features[11],
            "Suspicious Words": features[12]
        })