import pytest

from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.subtitle import Subtitle
from domainmodel.user import Movie, Review, User
from domainmodel.watchlist import WatchList

@pytest.fixture
def subtitle():
    return Subtitle("  English", "Good morning")

def test_constructor(subtitle):
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
