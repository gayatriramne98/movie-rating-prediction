# 🎬 Movie Review Rating Predictor

This project predicts user ratings for Harry Potter movie reviews using machine learning and a Streamlit web app.

---

## 📊 Dataset

- **Source:** `harry_potter_reviews.csv`
- **Fields:** `comment`, `rating`, `user_id`, etc.
- **Goal:** Use the `comment` text to predict the `rating`

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


## 🔬 Notebooks and Code

- `movie_rating_prediction.ipynb`: Full training notebook (Google Colab)
- `app.py`: Streamlit app for real-time prediction
- `movie_rating_model.pkl`: Saved ML model
- `tfidf_vectorizer.pkl`: Saved text vectorizer



## 📈 Example Plot

![Actual vs Predicted](images/actual_vs_predicted.png) <!-- optional image -->

---

## 🔧 How to Run Locally

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
streamlit run app.py
# movie-rating-prediction
Predicting movie ratings from reviews using machine learning
