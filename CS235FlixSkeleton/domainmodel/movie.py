from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.subtitle import Subtitle
from typing import List, Iterable



class Movie:
    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

        if type(release_year) is not int or release_year <= 1899:
            self.__release_year = None
        else:
            self.__release_year = release_year

        self.__actors = list()
        self.__genres = list()
        self.__subtitles = list()
        self.__director = None
        self.__description = None
        self.__runtime_minutes = 0


    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description.strip()
    
    @property
    def director(self):
        return self.__director
    
    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @property
    def actors(self):
        return self.__actors
    
    @property
    def genres(self):
        return self.__genres

    @property
    def subtitles(self):
        return self.__subtitles

    @title.setter
    def title(self, title):
        self.__title = title

    @release_year.setter
    def release_year(self, year):
        if year <= 1899:
            year = None
        self.__release_year = year
    
    @description.setter
    def description(self, desc):
        self.__description = desc.strip()

    @director.setter
    def director(self, director):
        self.__director = director

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if time <= 0:
            raise ValueError("Must be positive")
        self.__runtime_minutes = time

    @actors.setter
    def actors(self, actors):
        self.__actors = actors
    
    @genres.setter
    def genres(self, genres):
        self.__genres = genres

    @subtitles.setter
    def subtitles(self, subs):
        self.__subtitles = subs
    
    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return other.__title == self.__title and other.__release_year == self.__release_year

    def __lt__(self, other):
        #return (self.__title < other.__title) or (self.__release_year < other.__release_year)
        return (self.__title, self.__release_year) < (other.__title, other.__release_year)

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

    def add_subtitle(self, subtitle: Subtitle):
        
        self.__subtitles.append(subtitle)

    def remove_subtitle(self, subtitle: Subtitle):
        if subtitle in self.__subtitles:
            self.__subtitles.remove(subtitle)