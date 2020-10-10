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
import CS235Flix.movies.services as movies_services
import CS235Flix.authentication.services as auth_services
import CS235Flix.watchlist.services as watchlist_services
from CS235Flix.authentication.services import AuthenticationException


# test authentication

def test_can_add_user(in_memory_repo):
    new_username = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    # Check that password has been encrypted.
    assert user_as_dict['password'].startswith('pbkdf2:sha256:')

def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)

def test_authentication_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except AuthenticationException:
        assert False

def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)

# test movies
def test_get_movie(in_memory_repo):
    movie = Movie('Guardians of the Galaxy', 2014)
    assert movies_services.get_movie(movie, in_memory_repo) == movie

def test_create_review(in_memory_repo):
    movie = Movie('Guardian of the galaxy', 2014)
    review_text = 'hello'
    rating = 10
    user = User('Paul', '1234')
    review = movies_services.create_review(movie, review_text, rating, user)
    assert type(review) == Review

def test_get_movie_id(in_memory_repo):
    movie = Movie('Guardians of the Galaxy', 2014)
    movie2 = movies_services.get_movie_by_id(1, in_memory_repo)
    assert movie == movie2

def test_add_review(in_memory_repo):
    review = Review(Movie('a', 1900), 'b', 1, User('c', 'd'))
    movies_services.add_review(review, in_memory_repo)
    assert in_memory_repo.get_number_of_reviews() == 1

def test_get_movies_by_actor(in_memory_repo):
    actor = 'Chris Pratt'
    movies = movies_services.get_movies_by_actor(actor, in_memory_repo)
    for movie in movies:
        assert actor in movie.actors

def test_get_movies_by_genre(in_memory_repo):
    genre = 'Action'
    movies = movies_services.get_movies_by_genre(genre, in_memory_repo)
    for movie in movies:
        assert genre in movie.genres

def test_get_movies_by_director(in_memory_repo):
    director = 'Peter Jackson'
    movies = movies_services.get_movies_by_director(director, in_memory_repo)
    for movie in movies:
        assert director == movie.director

def test_get_movies_by_rating(in_memory_repo):
    movies = movies_services.get_movies_by_rating(in_memory_repo)
    for i in range(len(movies) -1):
        assert movies[i].rating >= movies[i+1].rating

def test_get_latest_movies(in_memory_repo):
    movies = movies_services.get_latest_movies(in_memory_repo)
    for i in range(len(movies) -1):
        assert movies[i].release_year >= movies[i+1].release_year

    
# test watchlist