import pytest
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.director import Director
from CS235Flix.domain.genre import Genre
from CS235Flix.domain.subtitle import Subtitle
from CS235Flix.domain.user import Movie, Review, User

@pytest.fixture
def movie():
    return Movie("Jaws", 1994)

@pytest.fixture
def actor():
    return Actor("James")

@pytest.fixture
def genre():
    return Genre("Action")

@pytest.fixture
def director():
    return Director("David")

@pytest.fixture
def subtitle():
    return Subtitle("  English", "Good morning")


def test_constructors(movie, genre, director, subtitle):
    assert movie.title == "Jaws"
    assert movie.release_year == 1994
    assert genre.genre_name == "Action"
    assert director.director_full_name == "David"
    assert subtitle._language == "english" 
    assert subtitle._transcript == "Good morning"

def test_add_to_movie(subtitle):
    movie = Movie("Jaws", 1975)
    assert len(movie.subtitles) == 0
    movie.add_subtitle(subtitle)
    assert len(movie.subtitles) == 1

def test_add_same_language(subtitle):
    subtitle2 = Subtitle("English", "Hello")
    movie = Movie("Jaws", 1975)
    movie.add_subtitle(subtitle)
    assert movie.subtitles[0].transcript == "Good morning"
    movie.add_subtitle(subtitle2)
    assert movie.subtitles[0].transcript == "Hello"

def test_remove_empty(subtitle):
    movie = Movie("Jaws", 1975)
    movie.remove_subtitle(subtitle)
    assert len(movie.subtitles) == 0

def test_equality(subtitle):
    subtitle2 = Subtitle("English", "Good morning")
    assert (subtitle == subtitle2) == True
    subtitle2 = Subtitle("   english", "Hello")
    assert (subtitle == subtitle2) == True
    subtitle2 = Subtitle("Spanish", "Hola")
    assert (subtitle == subtitle2) == False
