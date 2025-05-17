import streamlit as st
import pickle
import numpy as np

# Load the trained model and vectorizer
model = pickle.load(open("movie_rating_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Streamlit UI
st.title("🎬 Movie Review Rating Predictor")
st.write("Enter your movie review below and get a predicted rating (1 to 10):")

# User input
review = st.text_area("✍️ Your Review:")

# Predict button
if st.button("Predict Rating"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        # Transform and predict
        review_transformed = vectorizer.transform([review])
        prediction = model.predict(review_transformed)
        st.success(f"🎯 Predicted Rating: {round(prediction[0], 2)} / 10")
