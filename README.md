# 🎬 Cinemagic AI – Movie Recommendation System

Discover your next favorite film with **content-based machine learning recommendations**.

Cinemagic AI is a Streamlit web app that suggests movies similar to the one you pick, using cosine similarity on movie metadata from the TMDB 5000 dataset. Posters are fetched live from the TMDB API.

---

## ✨ Features

- 🔍 Select or type any movie from the dropdown
- 🤖 Get 5 similar movie recommendations instantly
- 🖼️ Movie posters fetched from the TMDB API
- 🎨 Modern dark UI with custom CSS and animations
- ⚡ Fast results using pre-computed similarity matrix

## 🧠 How It Works

1. **Data**: TMDB 5000 Movies and Credits datasets
2. **Preprocessing**: Merge datasets and combine overview, genres, keywords, cast and crew into a single `tags` column
3. **Vectorization**: Convert tags into vectors (Bag of Words / CountVectorizer)
4. **Similarity**: Compute cosine similarity between all movies
5. **Recommendation**: Return the top 5 movies with the highest similarity score to the selected movie

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.13 |
| Web App | Streamlit |
| Data | Pandas, NumPy |
| ML | Scikit-learn, NLTK |
| API | TMDB API |
| Tools | Jupyter Notebook, VS Code, Git |

## 📁 Project Structure

```
cinemagic-ai-movie-recommender/
├── app.py                  # Streamlit application
├── moviee.ipynb            # Data processing & model building notebook
├── movie_dict.pkl          # Processed movie data
├── similarity.pkl          # Cosine similarity matrix
├── tmdb_5000_movies.csv    # Dataset
├── tmdb_5000_credits.csv   # Dataset
├── requirements.txt        # Dependencies
├── Procfile                # Deployment config
└── README.md
```

## 🚀 Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/cinemagic-ai-movie-recommender.git
cd cinemagic-ai-movie-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

## 🔑 TMDB API Key

The app uses the TMDB API for posters. Get a free key at [themoviedb.org](https://www.themoviedb.org/settings/api) and add it in `app.py` (or better, store it as an environment variable / Streamlit secret — never commit your key).

## 📸 Screenshots

![Home Screen](screenshots/home.png)

## ⚠️ Limitations

- Content-based only (does not use user ratings or history)
- Limited to the ~5000 movies in the dataset
- Some movies have no poster available

## 🔮 Future Improvements

- Hybrid recommendation (collaborative + content-based)
- Search by genre, actor or director
- Larger dataset and movie details (rating, overview, trailer)
- Deployment on Streamlit Community Cloud

## 👩‍💻 Author

**Antra Roy**
BCA (Data Science), Chandigarh University
📧 antraroy@gmail.com

---
⭐ If you like this project, give it a star!