import abc

from CS235Flix.domain.user import User
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.director import Director
from CS235Flix.domain.genre import Genre
from CS235Flix.domain.review import Review

repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie:Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie:Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor:Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor:Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review:Review):
        raise NotImplementedError

    @abc.abstractmethod
    def get_review(self, review:Review):
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director:Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director:Director):
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre:Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self, genre:Genre):
        raise NotImplementedError

    @abc.abstractmethod   
    def get_number_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_actors(self):
        raise NotImplementedError

    @abc.abstractmethod     
    def get_number_of_reviews(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_number_of_directors(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_number_of_genres(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_actor(self, actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_genre(self, genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_director(self, director):
        raise NotImplementedError  

    @abc.abstractmethod
    def get_movies_by_rating(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_runtime(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_latest_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_actors(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_genres(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_directors(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_movie_ids(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ids(self):
        raise NotImplementedError
