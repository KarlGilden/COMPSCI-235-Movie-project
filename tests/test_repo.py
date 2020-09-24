import pytest
import os
from CS235Flix.adapters.memory_repository import MemoryRepository, populate
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor 
from CS235Flix.domain.genre import Genre 
from CS235Flix.domain.director import Director 
from CS235Flix.domain.review import Review 
from CS235Flix.domain.user import User 
import CS235Flix.adapters.repository as repos



@pytest.fixture
def repo():
    data_path = os.path.join('CS235Flix', 'datafiles')
    repos.repo_instance = MemoryRepository()
    populate(data_path, repos.repo_instance)
    repo = repos.repo_instance
    return repo

def test_in_repo(repo):
    assert repo.get_number_of_movies() == 1000
    assert repo.get_number_of_genres() == 20
    assert repo.get_number_of_actors() == 1985
    assert repo.get_number_of_directors() == 644

def test_add_movie(repo):
    repo.add_movie(Movie('Joker', 2019))
    assert repo.get_number_of_movies() == 1001

def test_cannot_add_duplicate_movies(repo):
    movie = Movie('Guardians of the Galaxy', 2014)
    repo.add_movie(movie)
    assert repo.get_number_of_movies() == 1000

def test_add_actor(repo):
    repo.add_actor(Actor('John Smith'))
    assert repo.get_number_of_actors() == 1986

def test_cannot_add_duplicate_actors(repo):
    actor = Actor('Chris Pratt')
    repo.add_actor(actor)
    assert repo.get_number_of_actors() == 1985

def test_add_genre(repo):
    repo.add_genre(Genre('Spaghetti Western'))
    assert repo.get_number_of_genres() == 21

def test_cannot_add_duplicate_genres(repo):
    genre = Genre('Action')
    repo.add_genre(genre)
    assert repo.get_number_of_genres() == 20

def test_add_director(repo):
    repo.add_director(Director('John Smith'))
    assert repo.get_number_of_directors() == 645 

def test_cannot_add_duplicate_directors(repo):
    director = Director('Peter Jackson')
    repo.add_director(director)
    assert repo.get_number_of_directors() == 644

def test_add_review(repo):
    movie = Movie('Guardians of the Galaxy', 2014)
    user = User('john smith', '1234')
    repo.add_review(Review(movie, 'this is a review', 10, user))
    assert repo.get_number_of_reviews() == 1 

def test_cannot_add_duplicate_reviews(repo):
    movie = Movie('Guardians of the Galaxy', 2014)
    user = User('john smith', '1234')
    review = Review(movie, 'this is a review', 10, user)
    repo.add_review(review)
    assert repo.get_number_of_reviews() == 1
    repo.add_review(review)
    assert repo.get_number_of_reviews() == 1

def test_get_movie(repo):
    repo.add_movie(Movie('Joker', 2019))
    assert str(repo.get_movie(Movie('Joker', 2019))) == "<Movie Joker, 2019>"

def test_get_movies_by_actors(repo):
    actor = 'Vin Diesel'
    movies = repo.get_movies_by_actor(actor)
    for i in range(len(movies)):
        assert actor in movies[i].actors

def test_get_movies_by_genres(repo):
    genre = 'Action'
    movies = repo.get_movies_by_actor(genre)
    for i in range(len(movies)):
        assert genre in movies[i].genres

def test_get_movies_by_director(repo):
    director = 'Michael Bay'
    movies = repo.get_movies_by_actor(director)
    for i in range(len(movies)):
        assert director == movies[i].director

def test_get_movies_by_rating(repo):
    movies = repo.get_movies_by_rating()
    for i in range(len(movies)-1):
        assert movies[i].rating >= movies[i + 1].rating

def test_get_movies_by_runtime(repo):
    movies = repo.get_movies_by_runtime()
    for i in range(len(movies)-1):
        assert movies[i].runtime_minutes >= movies[i + 1].runtime_minutes