from .repository import AbstractRepository, RepositoryException
from CS235Flix.domain.user import User
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.director import Director
from CS235Flix.domain.genre import Genre
from CS235Flix.domain.review import Review
from CS235Flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
import CS235Flix.datafiles
import os




class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__movies = list()
        self.__movie_ids = dict()
        self.__genres = list()
        self.__reviews = list()
        self.__actors = list()
        self.__directors = list()
        self.__users = list()


    def add_user(self, user):
        if user not in self.__users:
            self.__users.append(user)

    def get_user(self, username):
        for user in self.__users:
            if user.user_name == username:
                return user
        return None

    def add_movie(self, movie:Movie):
        if movie not in self.__movies:
            self.__movies.append(movie)

    def get_movie(self, movie:Movie):
        if type(movie) == int:
            try:
                return self.__movies[movie]
            except:
                return None
        else:
            try:
                index = self.__movies.index(movie)
                return self.__movies[index]
            except:
                return None

    def add_actor(self, actor:Actor):
        if actor not in self.__actors:
            self.__actors.append(actor)

    def get_actor(self, actor:Actor):
        if type(actor) == int:
            try:
                return self.__actors[actor]
            except:
                return None
        else:
            try:
                index = self.__actors.index(actor)
                return self.__actors[index]
            except:
                return None

    def add_review(self, review:Review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    def get_review(self, review:Review):
        if type(review) == int:
            try:
                return self.__reviews[review]
            except:
                return None
        else:
            try:
                index = self.__reviews.index(review)
                return self.__reviews[index]
            except:
                return None

    def add_director(self, director:Director):
        if director not in self.__directors:
            self.__directors.append(director)

    def get_director(self, director:Director):
        if type(director) == int:
            try:
                return self.__directors[director]
            except:
                return None
        else:
            try:
                index = self.__directors.index(director)
                return self.__directors[index]
            except:
                return None

    def add_genre(self, genre:Genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    def get_genre(self, genre:Genre):
        if type(genre) == int:
            try:
                return self.__genres[genre]
            except:
                return None
        else:
            try:
                index = self.__genres.index(genre)
                return self.__genres[index]
            except:
                return None
            
    def get_number_of_movies(self):
        return len(self.__movies)

    def get_number_of_actors(self):
        return len(self.__actors)

    def get_number_of_reviews(self):
        return len(self.__reviews)
    
    def get_number_of_directors(self):
        return len(self.__directors)
    
    def get_number_of_genres(self):
        return len(self.__genres)


    # search functions

    def get_movies_by_actor(self, actor):
        movies = []
        for i in range(len(self.__movies)):
            for j in range(len(self.__movies[i].actors)):
                if Actor(actor) == Actor(self.__movies[i].actors[j]):
                    movies.append(self.__movies[i])
        return movies
        
    def get_movies_by_genre(self, genre):
        movies = []
        for i in range(len(self.__movies)):
            for j in range(len(self.__movies[i].genres)):
                if Genre(genre) == Genre(self.__movies[i].genres[j]):
                    movies.append(self.__movies[i])
        return movies

    def get_movies_by_director(self, director):
        return [movie for movie in self.__movies if Director(director) == movie.director]

    def get_movies_by_rating(self):
        return sorted(self.__movies, key=lambda movie: movie.rating, reverse=True)

    def get_movies_by_runtime(self):
        return sorted(self.__movies, key=lambda movie: movie.runtime_minutes, reverse=True)

    def get_movie_by_id(self, id):
        if id in self.__movie_ids:
            return self.__movie_ids[id]

    def get_latest_movies(self):
        return sorted(self.__movies, key=lambda movie: movie.release_year, reverse=True)

    def get_all_movies(self):
        return self.__movies

    def get_all_actors(self):
        return self.__actors

    def get_all_genres(self):
        return self.__genres

    def get_all_directors(self):
        return self.__directors

    def create_movie_ids(self):
        for movie in self.__movies:
            self.__movie_ids[movie.id] = movie

    def get_movie_ids(self):
        return self.__movie_ids

# load repository

def load_movies(datapath, repo):
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(os.path.join(datapath, filename))
    movie_file_reader.read_csv_file()
    for movie in movie_file_reader.dataset_of_movies:
        repo.add_movie(movie)
    repo.create_movie_ids()

def load_genres(datapath, repo):
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(os.path.join(datapath, filename))
    movie_file_reader.read_csv_file()
    for genre in movie_file_reader.dataset_of_genres:
        repo.add_genre(genre)

def load_actors(datapath, repo):
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(os.path.join(datapath, filename))
    movie_file_reader.read_csv_file()
    for actor in movie_file_reader.dataset_of_actors:
        repo.add_actor(actor)

def load_directors(datapath, repo):
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(os.path.join(datapath, filename))
    movie_file_reader.read_csv_file()
    for director in movie_file_reader.dataset_of_directors:
        repo.add_director(director)

def populate(datapath, repo):
    load_movies(datapath, repo)
    load_genres(datapath, repo)
    load_actors(datapath, repo)
    load_directors(datapath, repo)
    repo.add_user(User("fmercury", "mvNNbc1eLA$i"))
    repo.add_user(User("thorke", "cLQ^C#oFXloS"))