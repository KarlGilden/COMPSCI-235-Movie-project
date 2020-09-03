import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.subtitle import Subtitle
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self._dataset_of_movies = []
        self._dataset_of_actors = set()
        self._dataset_of_directors = set()
        self._dataset_of_genres = set()
        self._dataset_of_subtitles = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)

                genres_str = row['Genre']
                genres = genres_str.split(',')

                director_str = row['Director']
                director = Director(director_str)

                actors_str = row['Actors']
                actors = actors_str.split(',')

                subtitles_str = row['Subtitles']
                if subtitles_str is None:
                    subtitles = ''
                else:
                    subtitles = subtitles_str.split(',')
               


                for a in actors:
                    a = a.strip()
                    self._dataset_of_actors.add(Actor(a))

                for g in genres:
                    self._dataset_of_genres.add(Genre(g))
                
                for s in subtitles:
                    self._dataset_of_subtitles.add(Subtitle(s, None))

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

    