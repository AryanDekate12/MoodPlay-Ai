import streamlit as st
import pickle

from api_utils import get_games
from trailer_utils import get_trailer
from mood_detection import detect_mood
from store_utils import get_store_links


# -----------------------------
# Load ML Models
# -----------------------------

model = pickle.load(open("models/mood_model.pkl", "rb"))
mood_encoder = pickle.load(open("models/mood_encoder.pkl", "rb"))
genre_encoder = pickle.load(open("models/genre_encoder.pkl", "rb"))


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="MoodPlay AI",
    page_icon="🎮",
    layout="wide"
)


# -----------------------------
# UI Styling
# -----------------------------

st.markdown("""
<style>

img {
border-radius: 15px;
}

.game-card {
background-color:#111;
padding:15px;
border-radius:12px;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------

st.title("🎮 MoodPlay AI")

st.subheader("AI Mood Based Game Recommendation System")

st.write(
"""
Describe how you feel and the system will recommend  
games based on your mood and device.
"""
)


# -----------------------------
# User Inputs
# -----------------------------

user_text = st.text_input(
"💬 How are you feeling today?",
placeholder="Example: I feel bored today"
)

device = st.selectbox(
"📱 Select your device",
["Mobile","Laptop"]
)


# -----------------------------
# Recommendation Trigger
# -----------------------------

recommend = False

if user_text:
    recommend = True


# -----------------------------
# Recommendation Logic
# -----------------------------

if recommend:

    mood = detect_mood(user_text)

    st.success(f"Detected Mood: **{mood.upper()}**")

    mood_encoded = mood_encoder.transform([mood])

    genre_pred = model.predict([[mood_encoded[0]]])

    genre = genre_encoder.inverse_transform(genre_pred)[0]

    st.info(f"Recommended Genre: **{genre}**")


    with st.spinner("Finding games for you..."):

        games = get_games(genre, device)


    if len(games) == 0:

        st.error("No games found.")

        st.stop()


    st.markdown("---")

    st.subheader("🎮 Recommended Games")


    # -----------------------------
    # Game Grid Layout
    # -----------------------------

    cols = st.columns(3)

    for index, game in enumerate(games):

        with cols[index % 3]:

            st.markdown(f"### 🎮 {game['name']}")

            if game["image"]:
                st.image(game["image"])

            st.write("⭐ Rating:", game["rating"])

            st.write("📅 Released:", game["released"])


            # -----------------------------
            # Game Trailer
            # -----------------------------

            trailer = get_trailer(game["name"])

            if trailer:
                st.video(trailer)


            # -----------------------------
            # Store Links
            # -----------------------------

            store_links = get_store_links(
                game["name"],
                game["stores"],
                device
            )

            if store_links:

                st.write("### 🎮 Available On")

                for store_name, link in store_links:

                    st.markdown(f"[Open on {store_name}]({link})")

            else:

                st.write("⚠ Not available on selected device")


            st.markdown("---")