# Movie_Recommendation_System
Explore a seamless movie recommendation system leveraging Streamlit and the TMDB dataset, delivering personalized film suggestions tailored to your tastes, enriching your cinematic exploration with meticulously curated selections catered uniquely to you.

 1. Clone the repository.

2. Download the movie dataset from the following URL: [Kaggle - TMDB Movie Metadata] # (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

3. Place the dataset in a folder named Dataset.

4. Install the dependencies listed in the requirements.txt file using the command:

    pip install -r requirements.txt

6. Obtain an API key for The Movie Database (TMDB) by signing up for an account on their website and generating an API key.

7. Paste the obtained API key into your app.py file where indicated, typically in a variable named TMDB_API_KEY.

8. Within your app.py file, locate the URL variable where the API request is made. It typically resembles:

    url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US".format(movie_id)
   
    Replace {TMDB_API_KEY} in the URL with your actual TMDB API key.

9. Once your app.py file is configured, navigate to your terminal within PyCharm or any other IDE, and execute the command to run the Streamlit app:

   1. python main.py

      Then two files will be genrated, then run 

   2. streamlit run app.py
    

