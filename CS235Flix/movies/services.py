from CS235Flix.adapters.repository import AbstractRepository
from CS235Flix.domain.review import Review
from CS235Flix.domain.movie import Movie

def get_movie(movie, repo):
    movie = repo.get_movie(movie)
    return movie

def create_review(movie, review_text, rating, user):
    review = Review(movie, review_text, rating, user)
    movie.add_review(review)
    return review

def get_movie_by_id(id, repo):
    return repo.get_movie_by_id(id)

def get_movie_ids(repo):
    return repo.get_movie_ids()

def add_review(review, repo):
    repo.add_review(review)

def create_movie(movie_id, repo):
    movie = repo.get_movie_ids()[movie_id]
    movie = repo.get_movie(movie)
    return movie

def get_movies_by_actor(actor, repo):
    movies = repo.get_movies_by_actor(actor)
    return movies

def get_movies_by_genre(genre, repo):
    movies = repo.get_movies_by_genre(genre)
    return movies

def get_movies_by_director(director, repo):
    movies = repo.get_movies_by_director(director)
    return movies

def get_movies_by_rating(repo):
    movies = repo.get_movies_by_rating()
    return movies

def get_top_50(repo):
    movies = get_movies_by_rating(repo)
    return movies[:50]

def get_top_20(repo):
    movies = get_movies_by_rating(repo)
    return movies[:20]

def get_latest_movies(repo):
    movies = repo.get_latest_movies()
    return movies

def get_movies_by_search(search, repo):
    movies = set()
    movies_by_actor = set(sorted(get_movies_by_actor(search, repo)))
    movies_by_director = set(sorted(get_movies_by_director(search, repo)))
    movies_by_genre = set(sorted(get_movies_by_genre(search, repo)))
    movies = movies.union(movies_by_actor).union(movies_by_director).union(movies_by_genre)
    return list(movies)
