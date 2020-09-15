from .movie import Movie
from .review import Review

class User:
    def __init__(self, user_name: str, password: str):
        self.__user_name = user_name.lower().strip()
        self.__password = password
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        if self.__time_spent_watching_movies_minutes < 0:
            self.__time_spent_watching_movies_minutes = 0
        return self.__time_spent_watching_movies_minutes

    @user_name.setter
    def user_name(self, name):
        self.__user_name = name

    @password.setter
    def password(self, password):
        self.__password = password

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        self.__watched_movies = watched_movies

    @reviews.setter
    def reviews(self, reviews):
        self.__reviews = reviews

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent_watching_movies_minutes):
        if time_spent_watching_movies_minutes < 0:
            time_spent_watching_movies_minutes = 0
        self.__time_spent_watching_movies_minutes = time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"
    
    def __eq__(self, other):
        return other.__user_name == self.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name
    
    def __hash__(self):
        return hash(self.__user_name)


    def watch_movie(self, movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        self.__reviews.append(review)