# 🎮 MoodPlay AI  
### AI Mood-Based Game Recommendation System

MoodPlay AI is an AI-powered web application that recommends games based on a user's **mood and preferred device (Mobile or Laptop)**.

The system detects the user's mood from text input using **Natural Language Processing (NLP)** and suggests games using **real-time game data APIs**.

The project is built with **Python, Machine Learning, NLP, and Streamlit** to create an interactive recommendation system.

---

# 🚀 Live Demo

When deployed on Streamlit Cloud, add your link here:

Try the app:  
https://game-suggestions.streamlit.app/

---

# 🎥 Project Demo



https://github.com/user-attachments/assets/876cfe05-ac04-47ae-872e-df5053b844d8



<video src="demo.mp4" controls width="800"></video>

---

# ✨ Features

- AI mood detection from text input
- Mood-based game recommendations
- Device selection (Mobile or Laptop)
- Real-time game data from API
- Game trailer previews
- Machine learning mood → genre mapping
- Streamlit interactive web interface
- Game store links when available
- Recommendation system using API data

---

# 🧠 How It Works

1. User enters their mood in text form.
2. NLP analyzes the text to detect the mood.
3. The machine learning model predicts a suitable game genre.
4. The system fetches real-time games from the API.
5. The application recommends games based on:
   - Mood
   - Device type
   - Game popularity
   - Rating and availability

---

# 🛠️ Tech Stack

Programming Language

- Python

Machine Learning

- Scikit-learn

Natural Language Processing

- TextBlob

Web Framework

- Streamlit

APIs

- RAWG Video Games Database API
- YouTube API (for game trailers)

Libraries

- pandas
- requests
- python-dotenv

---

# 📦 Installation

Clone the repository:

git clone https://github.com/AryanDekate12/MoodPlay-AI.git

Move into the project folder:

cd MoodPlay-AI

Install dependencies:

pip install -r requirements.txt

Download NLP corpora:

python -m textblob.download_corpora

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

RAWG_API_KEY=your_rawg_api_key

YOUTUBE_API_KEY=your_youtube_api_key

.env is ignored by GitHub for security.

---

# ▶️ Run The App

Start the Streamlit application:

streamlit run app.py

The app will open in your browser.

---

# 📁 Project Structure
```
MoodPlay-AI
│
├── models
│   ├── mood_model.pkl
│   ├── mood_encoder.pkl
│   └── genre_encoder.pkl
│
├── notebooks
│   └── mood_model_training.ipynb
│
├── app.py
├── api_utils.py
├── mood_detection.py
├── store_utils.py
├── trailer_utils.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example

```
---

# 🔮 Future Improvements

- Face-based emotion detection using webcam
- Personalized recommendations using user history
- Game popularity analytics dashboard
- Advanced ML recommendation engine
- User login and profiles
- Game filtering by genre and ratings

---

# 👨‍💻 Author

Aryan Dekate

GitHub:  
https://github.com/AryanDekate12

---

# ⭐ Support

If you like this project, consider starring the repository.
