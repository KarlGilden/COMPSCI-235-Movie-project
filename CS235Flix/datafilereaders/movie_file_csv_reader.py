import csv

from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.genre import Genre
from CS235Flix.domain.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self._dataset_of_movies = []
        self._dataset_of_actors = set()
        self._dataset_of_directors = set()
        self._dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                rating = float(row['Rating'])
                runtime = int(row['Runtime (Minutes)'])
                id = int(row['Rank'])
                description = row['Description']
                movie = Movie(title, release_year)
                movie.rating = rating
                movie.runtime_minutes = runtime
                movie.id = id
                movie.description = description
                genres_str = row['Genre']
                genres = genres_str.split(',')

                director_str = row['Director']
                director = Director(director_str)

                actors_str = row['Actors']
                actors = actors_str.split(',')



                for a in actors:
                    a = a.strip()
                    if a not in movie.actors:
                        movie.add_actor(a)
                    self._dataset_of_actors.add(Actor(a))

                for g in genres:
                    if g not in movie.genres:
                        movie.add_genre(g)
                    self._dataset_of_genres.add(Genre(g))

                movie.director = director
                
                if movie not in self._dataset_of_movies:
                    self._dataset_of_movies.append(movie)
                    
                self._dataset_of_directors.add(director)
            
                index += 1


    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self._dataset_of_genres

    @dataset_of_movies.setter
    def dataset_of_movies(self, movies):
        self._dataset_of_movies = movies

    @dataset_of_actors.setter
    def dataset_of_actors(self, actors):
        self._dataset_of_actors = actors

    @dataset_of_directors.setter
    def dataset_of_directors(self, directors):
        self._dataset_of_directors = directors

    @dataset_of_genres.setter
    def dataset_of_genres(self, genres):
        self._dataset_of_genres = genres
