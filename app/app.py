import streamlit as st
import pickle
import requests
import gzip


with gzip.open('movies.pkl.gz', 'rb') as f:
    movies_list = pickle.load(f)
display_list = movies_list['title'].values

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)


def tmdb_webpage(movie_id):
    return f"https://www.themoviedb.org/movie/{movie_id}"

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=6936587bb902958fe77aa8c09c006960".format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_links = []
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_links.append(tmdb_webpage(movie_id))
    
    return recommended_movies, recommended_movies_posters, recommended_movies_links


# Background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #17032b, #2b032a);
        color: white;
    }
    .big-font {
        font-size: 18px !important;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title('🎬Movie Recommendation System')
st.markdown("""
    <div class="big-font">
    Discover movies similar to your favorite picks! Select a movie below and click "Recommend" to get started.
    </div>
    """, unsafe_allow_html=True)


selected_movie = st.selectbox(
    "🎥 Select your Movie",
    display_list,
    help="Choose a movie to get recommendations"
)


# Recommendation button
if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        names, posters, links = recommend(selected_movie)
    cols = st.columns(len(names))
    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <style>
                .movie-card {{
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    transition: transform 0.2s, box-shadow 0.2s;
                }}
                .movie-card:hover {{
                    transform: scale(1.05);
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
                }}
                .movie-title {{
                    text-align: center;
                    font-size: 16px;
                    color: white;
                    margin-top: 10px;
                }}
                </style>
                <div class="movie-card">
                    <a href="{links[i]}">
                        <img src="{posters[i]}" style="width:100%; display:block;">
                    </a>
                </div>
                <div class="movie-title">{names[i]}</div>
                """,
                unsafe_allow_html=True
            )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: white;">
        Made with ❤️ by G0zi | Powered by <a href="https://www.themoviedb.org/" target="_blank">TMDB</a>
    </div>
    """,
    unsafe_allow_html=True
)