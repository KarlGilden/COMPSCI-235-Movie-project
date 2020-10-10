import pytest
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.director import Director
from CS235Flix.domain.genre import Genre
from CS235Flix.domain.subtitle import Subtitle
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.review import Review
from CS235Flix.domain.user import User
from CS235Flix.domain.watchlist import WatchList


@pytest.fixture
def movie():
    return Movie("Jaws", 1975)

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
def review(movie, user):
    return Review(movie, 'hello', 0, user)

@pytest.fixture
def user():
    return User('John Smith', '1234')

# test construtors for all domain classes
def test_constructors(movie, genre, actor, director, review):
    assert movie.title == "Jaws"
    assert movie.release_year == 1975
    assert actor.actor_full_name == "James"
    assert genre.genre_name == "Action"
    assert director.director_full_name == "David"
    assert review.review_text == "hello"

# test movie class
def test_add_movie_lists(movie, actor, genre, review):
    assert len(movie.actors) == 0
    assert len(movie.genres) == 0
    assert len(movie.reviews) == 0
    movie.add_actor(actor)
    movie.add_genre(genre)
    movie.add_review(review)
    assert len(movie.actors) == 1
    assert len(movie.genres) == 1
    assert len(movie.reviews) == 1

def test_remove_movie_lists(movie, actor, genre, review):
    movie.add_actor(actor)
    movie.add_genre(genre)
    movie.add_review(review)
    assert len(movie.actors) == 1
    assert len(movie.genres) == 1
    assert len(movie.reviews) == 1
    movie.remove_actor(actor)
    movie.remove_genre(genre)
    movie.remove_review(review)
    assert len(movie.actors) == 0
    assert len(movie.genres) == 0
    assert len(movie.reviews) == 0

def test_setter_function(movie, actor, genre, review, director):
    assert movie.title == 'Jaws'
    assert movie.release_year == 1975
    assert movie.director == None
    assert movie.description == str()
    assert movie.rating == 0
    assert movie.runtime_minutes == 0
    assert movie.id == 0
    movie.title = 'Jaws 2'
    movie.release_year = 1978
    movie.director = director
    movie.description = 'a movie'
    movie.rating = 10
    movie.runtime_minutes = 90
    movie.id = 3
    assert movie.title == 'Jaws 2'
    assert movie.release_year == 1978
    assert str(movie.director) == '<Director David>'
    assert movie.description == 'a movie'
    assert movie.rating == 10
    assert movie.runtime_minutes == 90
    assert movie.id == 3


def test__movie_eq_lt_repr(movie):
    movie2 = Movie(movie.title, movie.release_year)
    assert movie == movie2
    movie2.release_year = 2020
    assert movie != movie2
    assert movie < movie2
    assert repr(movie) == "<Movie Jaws, 1975>"

# test actor class

def test_actor_setter(actor):
    assert actor.actor_full_name == "James"
    actor.actor_full_name = "Bob"
    assert actor.actor_full_name == "Bob"

def test_add_colleague(actor):
    colleague = Actor('Collin')
    assert len(actor.colleagues) == 0
    actor.add_actor_colleague(colleague)
    assert len(actor.colleagues) == 1
    assert actor.check_if_this_actor_worked_with(colleague) == True

def test_actor_eq_lt_repr(actor):
    actor2 = Actor('James')
    assert actor2 == actor
    actor2.actor_full_name = 'Uri' 
    assert actor < actor2
    assert repr(actor) == "<Actor James>"

# test genre class

def test_genre_setter(genre):
    assert genre.genre_name == "Action"
    genre.genre_name = "Sci-fi"
    assert genre.genre_name == "Sci-fi"

def test_genre_eq_lt_repr(genre):
    genre2 = Genre('Action')
    assert genre2 == genre
    genre2.genre_name = 'Sci-fi' 
    assert genre < genre2
    assert repr(genre) == "<Genre Action>"


# test director class


def test_director_setter(director):
    assert director.director_full_name == "David"
    director.director_full_name = "Peter Jackson"
    assert director.director_full_name == "Peter Jackson"

def test_director_eq_lt_repr(director):
    director2 = Director('David')
    assert director2 == director
    director2.director_full_name = 'Peter Jackson' 
    assert director < director2
    assert repr(director) == "<Director David>"

# test review class

def test_constructor(review, movie, user):
    assert review.movie == movie
    assert review.user == user
    assert review.review_text == 'hello'
    assert review.rating == None
    review.rating = 1
    assert review.rating == 1

def test_setters(review):
    review.movie = Movie('Jaws 2', 1978)
    review.user = User("Bob", "the builder")
    review.review_text = 'yes we can'
    review.rating = 10
    assert repr(review.movie) == "<Movie Jaws 2, 1978>"
    assert repr(review.user) == "<User Bob>"
    assert review.review_text == 'yes we can'
    assert review.rating == 10

def test_eq_repr(review):
    review2 = review
    assert review == review2
    review2.review_text = 'sharks'
    assert review2 == review
    assert repr(review) == f"<<Movie Jaws, 1975>, {review.timestamp}>"

# test user class

def test_user_constructor(user):
    assert user.user_name == 'John Smith'
    assert user.password == '1234'
    assert len(user.watched_movies) == 0
    assert len(user.reviews) == 0
    assert user.time_spent_watching_movies_minutes == 0
    assert user.watchlist.size() == 0

def test_user_setter(user):
    user.user_name = 'Bart Simpson'
    user.password = 'kool'
    user.time_spent_watching_movies_minutes = 1000
    assert user.user_name == 'Bart Simpson'
    assert user.password == 'kool'
    assert user.time_spent_watching_movies_minutes == 1000

def test_user_add_lists(user, movie, review):
    assert len(user.watched_movies) == 0
    assert len(user.reviews) == 0
    user.watch_movie(movie)
    user.add_review(review)
    assert len(user.watched_movies) == 1
    assert len(user.reviews) == 1
    