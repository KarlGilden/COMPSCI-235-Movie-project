from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text
        self.__timestamp = datetime.now()
        if rating >= 1 and rating <=10:
            self.__rating = rating
        else:
            self.__rating = None

    def __repr__(self):
       return f"<{self.__movie}, {self.__timestamp}>"

    def __eq__(self, other):
        if self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp:
            return True
        else:
            return False

    @property
    def movie(self):
        return self.__movie
    
    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    @movie.setter
    def movie(self, movie):
        self.__movie = movie
    
    @review_text.setter
    def review_text(self, text):
        self.__review_text = text

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp