import streamlit as st
import pickle
import pandas as pd
import requests

# Page Configuration
st.set_page_config(
    page_title="Cinemagic | AI Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Attractive Interface, Animations, and Movie Cards
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Animated Title Header */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .header-container {
        animation: fadeInDown 0.8s ease-out;
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 50%, #0f172a 100%);
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #f43f5e, #fb7185, #f43f5e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
    }

    /* Movie Card Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .movie-card {
        background: #1e293b;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeInUp 0.6s ease-out forwards;
        border: 1px solid rgba(255, 255, 255, 0.05);
        height: 100%;
    }

    .movie-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 30px rgba(244, 63, 94, 0.3);
        border-color: rgba(244, 63, 94, 0.4);
    }

    .movie-title {
        font-weight: 600;
        font-size: 0.95rem;
        color: #f1f5f9;
        margin-top: 10px;
        margin-bottom: 5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Custom Streamlit Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(244, 63, 94, 0.4);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
        box-shadow: 0 6px 20px rgba(244, 63, 94, 0.6);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# TMDB Poster Fetcher Function
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": "7498b676ecc97a38929c42ead66d7a54",
        "language": "en-US"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print("TMDB Error:", e)
        return "https://via.placeholder.com/500x750?text=No+Poster"

# Recommendation Logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load pickled data
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies_df = pd.DataFrame(movies_dict)
    similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
    return movies_df, similarity_matrix

movies, similarity = load_data()

# App Header
st.markdown("""
    <div class="header-container">
        <div class="header-title">🎬 Cinemagic AI</div>
        <div class="header-subtitle">Discover Your Next Favorite Film with Content-Based Machine Learning Recommendations</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar controls
st.sidebar.markdown("### 🎛️ Recommendation Controls")
selected_movie_name = st.sidebar.selectbox(
    "Select or type a movie you like:",
    movies["title"].values
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Developer Info")
st.sidebar.markdown("**Name:** Antra Roy")
st.sidebar.markdown("**Contact:** antraroy@gmail.com")
st.sidebar.markdown("[🔗 View Portfolio Project](#)")

# Main Layout
if st.button('✨ Generate Recommendations'):
    with st.spinner('Analyzing cinematic patterns and fetching posters...'):
        names, posters = recommend(selected_movie_name)
    
    st.markdown(f"### Because you enjoyed *{selected_movie_name}*, you might love:")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
                <div class="movie-card">
                    <img src="{posters[idx]}" style="width:100%; border-radius:8px; height: 270px; object-fit: cover;">
                    <div class="movie-title" title="{names[idx]}">{names[idx]}</div>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>Built with Python, Streamlit, and TMDB API | Designed by Antra Roy</p>", unsafe_allow_html=True)