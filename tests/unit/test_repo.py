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

# users
def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user

def test_repository_can_retrieve_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)
    user = in_memory_repo.get_user('Dave')
    assert user == User('Dave', '123456789')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


# movies
def test_repository_can_get_all_movies(in_memory_repo):
    assert len(in_memory_repo.get_all_movies()) == 10

def test_repository_can_retrieve_movie_count(in_memory_repo):
    count = in_memory_repo.get_number_of_movies()
    assert count == 10

def test_repository_can_add_movie(in_memory_repo):
    movie = Movie('Joker', 2019)
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_movie(Movie('Joker', 2019)) is movie

def test_repository_can_retrieve_movie_by_id(in_memory_repo):
    movie = Movie('Passengers', 2016)
    movie = in_memory_repo.get_movie(movie)
    assert in_memory_repo.get_movie_by_id(movie.id) is movie

def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(11)
    assert movie is None

def test_repository_can_get_movies_by_genre(in_memory_repo):
    movies = in_memory_repo.get_movies_by_genre('Action')
    assert len(movies) == 4

def test_repository_can_get_movies_by_actor(in_memory_repo):
    movies = in_memory_repo.get_movies_by_actor('Chris Pratt')
    assert len(movies) == 2

def test_repository_can_get_movies_by_director(in_memory_repo):
    movies = in_memory_repo.get_movies_by_director('James Gunn')
    assert len(movies) == 1

def test_repository_can_get_movies_by_rating(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rating()
    assert len(movies) == 10
    movie1 = movies[0]
    movie2 = movies[9]
    assert movie1.rating > movie2.rating

def test_repository_can_get_movies_by_runtime(in_memory_repo):
    movies = in_memory_repo.get_movies_by_runtime()
    assert len(movies) == 10
    movie1 = movies[0]
    movie2 = movies[9]
    assert movie1.runtime_minutes > movie2.runtime_minutes

def test_repository_can_get_latest_movies(in_memory_repo):
    movies = in_memory_repo.get_latest_movies()
    assert len(movies) == 10
    movie1 = movies[0]
    movie2 = movies[9]
    assert movie1.release_year > movie2.release_year

# actors

def test_repository_can_get_all_actors(in_memory_repo):
    actors = in_memory_repo.get_all_actors()
    assert len(actors) == 39

def test_repository_can_retrieve_actor_count(in_memory_repo):
    count = in_memory_repo.get_number_of_actors()
    assert count == 39

def test_repository_can_add_actor(in_memory_repo):
    actor = Actor('Bob')
    in_memory_repo.add_actor(actor)
    assert in_memory_repo.get_actor(actor) is actor

def test_repository_can_retrieve_actor(in_memory_repo):
    actor = Actor('Chris Pratt')
    assert in_memory_repo.get_actor(actor) == actor

def test_repository_does_not_retrieve_a_non_existent_actor(in_memory_repo):
    actor = in_memory_repo.get_actor(Actor('Bob'))
    assert actor is None

# genres

def test_repository_can_get_all_genres(in_memory_repo):
    assert len(in_memory_repo.get_all_genres()) == 14

def test_repository_can_retrieve_genres_count(in_memory_repo):
    count = in_memory_repo.get_number_of_genres()
    assert count == 14

def test_repository_can_add_genre(in_memory_repo):
    genre = Genre('ZoomZoom')
    in_memory_repo.add_genre(genre)
    assert in_memory_repo.get_genre(genre) is genre

def test_repository_can_retrieve_genre(in_memory_repo):
    genre = Genre('Action')
    assert in_memory_repo.get_genre(genre) == genre

def test_repository_does_not_retrieve_a_non_existent_genre(in_memory_repo):
    genre = in_memory_repo.get_genre(Genre('ZoomZoom'))
    assert genre is None

# directors

def test_repository_can_get_all_directors(in_memory_repo):
    assert len(in_memory_repo.get_all_directors()) == 10

def test_repository_can_retrieve_directors_count(in_memory_repo):
    count = in_memory_repo.get_number_of_directors()
    assert count == 10

def test_repository_can_add_directors(in_memory_repo):
    director = Director('John')
    in_memory_repo.add_director(director)
    assert in_memory_repo.get_director(director) is director

def test_repository_can_retrieve_director(in_memory_repo):
    director = Director('James Gunn')
    assert in_memory_repo.get_director(director) == director

def test_repository_does_not_retrieve_a_non_existent_director(in_memory_repo):
    director = in_memory_repo.get_director(Director('John'))
    assert director is None

# directors

def test_add_review(in_memory_repo):
    movie = Movie("Jaws", 1975)
    user = User("bob", "1242")
    review = Review(movie, 'hello', 10, user)
    in_memory_repo.add_review(review)
    assert in_memory_repo.get_number_of_reviews() == 1

