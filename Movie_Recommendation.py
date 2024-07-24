from flask import Flask, request, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__)

# Load the movie data
movies = pd.read_csv('movies.csv')

def get_recommendations(movie_name):
    return movies[movies['title'].str.contains(movie_name, case=False)]['title'].tolist()

def get_movie_details(movie_title):
    movie = movies[movies['title'] == movie_title].to_dict('records')
    if movie:
        movie_details = movie[0]
        return {
            'title': movie_details.get('title', 'N/A'),
            'description': movie_details.get('overview', 'Description not available'),
            'year': movie_details.get('release_date', 'Year not available').split('-')[0] if movie_details.get('release_date') else 'Year not available',
            'cast': movie_details.get('cast', 'Cast not available'),
            'director': movie_details.get('director', 'Director not available'),
            'genres': movie_details.get('genres', 'Genres not available'),
            'runtime': movie_details.get('runtime', 'Runtime not available'),
            'vote_average': movie_details.get('vote_average', 'Vote average not available')
        }
    return {}

@app.route('/')
def index():
    return send_from_directory('.', 'Movie_Recommendation.html')

@app.route('/Movie_Recommendation.css')
def styles():
    return send_from_directory('.', 'Movie_Recommendation.css')

@app.route('/Movie_Recommendation.js')
def script():
    return send_from_directory('.', 'Movie_Recommendation.js')

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie')
    recommendations = get_recommendations(movie_name)
    return jsonify({'recommendations': recommendations})

@app.route('/details', methods=['GET'])
def details():
    movie_title = request.args.get('title')
    movie_details = get_movie_details(movie_title)
    return jsonify(movie_details)

if __name__ == '__main__':
    app.run(debug=True)
