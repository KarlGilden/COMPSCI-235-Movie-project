import pytest
import os
from CS235Flix.adapters.memory_repository import MemoryRepository, populate
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor 
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

def test_add_movie(repo):
    repo.add_movie(Movie('Joker', 2019))
    assert repo.get_number_of_movies() == 1001

def test_get_movie(repo):
    repo.add_movie(Movie('Joker', 2019))
    assert str(repo.get_movie(1000)) == "<Movie Joker, 2019>"

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