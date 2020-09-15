from .repository import AbstractRepository, RepositoryException
from CS235Flix.domain.user import User
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.director import Director
from CS235Flix.domain.genre import Genre
from CS235Flix.domain.subtitle import Subtitle
from CS235Flix.domain.review import Review
from CS235Flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
import CS235Flix.datafiles
import os


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__movies = list()
        self.__genres = list()
        self.__reviews = list()
        self.__actors = list()
        self.__directors = list()
        self.__users = list()
        self.__subtitles = list()


    def add_user(self, user:User):
        if user not in self.__users:
            self.__users.append(user)

    def get_user(self, user):
        raise NotImplementedError

    def add_movie(self, movie:Movie):
        if movie not in self.__movies:
            self.__movies.append(movie)

    def get_movie(self, index:int):
        return self.__movies[index]

    def add_actor(self, actor:Actor):
        if actor not in self.__actors:
            self.__actors.append(actor)

    def get_actor(self, actor:Actor):
        raise NotImplementedError

    def add_review(self, review:Review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    def get_review(self, review:Review):
        raise NotImplementedError

    def add_director(self, director:Director):
        if director not in self.__directors:
            self.__directors.append(director)

    def get_director(self, director:Director):
        raise NotImplementedError

    def add_genre(self, genre:Genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    def get_genre(self, genre:Genre):
        raise NotImplementedError

    def add_subtitle(self, subtitle:Subtitle):
        if subtitle not in self.__subtitles:
            self.__subtitles.append(subtitle)

    def get_subtitle(self, subtitle:Subtitle):
        raise NotImplementedError

    def get_number_of_movies(self):
        return len(self.__movies)

    def get_movies_by_actor(self, actor):
        return [movie for movie in self.__movies if actor in movie.actors]
        
    def get_movies_by_genre(self, genre):
        return [movie for movie in self.__movies if genre in movie.genres]

    def get_movies_by_director(self, director):
        return [movie for movie in self.__movies if director == movie.director]

    def get_movies_by_rating(self):
        return sorted(self.__movies, key=lambda movie: movie.rating, reverse=True)

    def get_movies_by_runtime(self):
        return sorted(self.__movies, key=lambda movie: movie.runtime_minutes, reverse=True)


def load_movies(datapath, repo):
        filename = 'Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(os.path.join(datapath, filename))
        movie_file_reader.read_csv_file()
        for movie in movie_file_reader.dataset_of_movies:
            repo.add_movie(movie)

def populate(datapath, repo):
    load_movies(datapath, repo)