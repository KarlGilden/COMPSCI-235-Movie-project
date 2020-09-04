from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.watchlist import WatchList
from domainmodel.subtitle import Subtitle
from flask import Flask, render_template
import csv


app = Flask(__name__)

filename = 'Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

movie = Movie("Jaws", 1999)
english_sub = Subtitle("english", "hello")
movie.add_subtitle(english_sub)
english_sub = Subtitle("english", "good morning")
movie.add_subtitle(english_sub)
print(movie.subtitles[0]._transcript)

@app.route('/')
def index():
    return render_template('index.html', data=sorted(movie_file_reader.dataset_of_actors))

if __name__ == "__main__":
    app.run(debug=True)




