# Sample data representing movies and their genres
movies_data = {
    'Extraction': {'genre': 'Action'},
    'The Hangover': {'genre': 'Comedy'},
    'La La Land': {'genre': 'Drama'},
    'Hitman': {'genre': 'Action'},
    'Ted': {'genre': 'Comedy'},
}

# Simple content-based recommendation system function
def content_based_movie_recommendation(user_preferences, movies_data):
    recommended_movies = []

    # Iterate through movies and recommend based on user's preferred genre
    for movie, features in movies_data.items():
        if 'genre' in user_preferences and user_preferences['genre'].lower() == features['genre'].lower():
            recommended_movies.append(movie)

    return recommended_movies

# Example user preferences
user_preferences = {'genre': 'Action'}

# Get movie recommendations for the user
movie_recommendations = content_based_movie_recommendation(user_preferences, movies_data)

# Print recommendations
if movie_recommendations:
    print(f"Recommended movies for the user based on genre preference: {movie_recommendations}")
else:
    print("No recommendations found.")
