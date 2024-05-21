# Movie_Recommendation_System
Explore a seamless movie recommendation system leveraging Streamlit and the TMDB dataset, delivering personalized film suggestions tailored to your tastes, enriching your cinematic exploration with meticulously curated selections catered uniquely to you.

# 1. Install the dependencies listed in the requirements.txt file using the command:
    pip install -r requirements.txt

# 2. Obtain an API key for The Movie Database (TMDB) by signing up for an account on their website and generating an API key.

# 3. Paste the obtained API key into your app.py file where indicated, typically in a variable named TMDB_API_KEY.

# 4. Within your app.py file, locate the URL variable where the API request is made, which typically resembles:

# 5. url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
     Replace {TMDB_API_KEY} in the URL with your actual TMDB API key.
# 6. Once your app.py file is configured, navigate to your terminal within PyCharm or any other IDE, and execute the command to run the Streamlit app:
    streamlit run app.py


