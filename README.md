# 🎬 Movie Review Rating Predictor

This project predicts user ratings for Harry Potter movie reviews using machine learning and a Streamlit web app.

---

## 📊 Dataset

- **Source:** `harry_potter_reviews.csv`  
- **Fields:** `comment`, `rating`, `user_id`, etc.  
- **Goal:** Use the `comment` text to predict the `rating`.

---

## 🧠 Model

- **Vectorizer:** TF-IDF  
- **Model:** Linear Regression  
- **Evaluation Metrics:**  
  - MAE (Mean Absolute Error)  
  - MSE (Mean Squared Error)  

---

## 💻 Live Demo

👉 [Try the Streamlit App](https://gayatriramne98-movie-rating-app-streamlit-app-b42lyp.streamlit.app/)  

Paste a movie review and get a predicted rating!

---

## 🔬 Notebooks and Code

- `movie_rating_prediction.ipynb`: Full training notebook (Google Colab)  
- `app.py`: Streamlit app for real-time prediction  
- `movie_rating_model.pkl`: Saved ML model  
- `tfidf_vectorizer.pkl`: Saved text vectorizer  

---

## 📈 Example Plot

![Actual vs Predicted](![actual_vs_predicted](https://github.com/user-attachments/assets/b5172617-4d0d-470e-9ba0-b6db9118a895)
)  

---

## 🔧 How to Run Locally

```bash
git clone https://github.com/gayatriramne98/movie-rating-prediction.git
cd movie-rating-prediction
pip install -r requirements.txt
streamlit run app.py

