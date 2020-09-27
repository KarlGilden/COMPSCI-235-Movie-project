from CS235Flix.adapters.repository import AbstractRepository
from CS235Flix.domain.review import Review
from CS235Flix.domain.movie import Movie
from CS235Flix.domain.actor import Actor
from CS235Flix.domain.director import Director
from CS235Flix.domain.genre import Genre
import random

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

def get_movies_by_search(search, setting, repo):
    if search == None:
        search = ''
    movies = repo.get_all_movies()
    
    # get specific movie
    for movie in movies:
        if search == movie.title:
            return [movie]
    # get movies by genre
    if repo.get_genre(Genre(search)):
        movies = repo.get_movies_by_genre(search)   
    # get movies by actor
    elif repo.get_actor(Actor(search)):
        movies = repo.get_movies_by_actor(search)
    # get movies by director
    elif repo.get_director(Director(search)):
        movies = repo.get_movies_by_director(search)
    # search could not be found
    elif search != '':
        return "No movies could be found, please check your spelling"

    # sort alphabetically 
    if setting == 'A-Z':
        return sorted(movies)
    # sort by most recent releases
    elif setting == 'most recent':
        return sorted(movies, key=lambda movie: movie.release_year, reverse=True)
    # sort by oldest movies first
    elif setting == 'oldest':
        return sorted(movies, key=lambda movie: movie.release_year, reverse=False)
    elif setting == 'rating':
        return sorted(movies, key=lambda movie: movie.rating, reverse=True)
    # sort in default order
    else:
        return movies

def split_pages(movies, num_pages):
    for i in range(0, len(movies), num_pages):  
        yield movies[i:i + num_pages] 
    
def create_browse_categories(repo):

    categories = dict()
    latest_movies = get_movies_by_search(None, 'most recent', repo)
    top_rated_movies = get_movies_by_search(None, 'rating', repo)

    rands = random.sample(range(0,len(repo.get_all_genres())), 3)
    genre1 = repo.get_genre(rands[0]).genre_name
    genre2 = repo.get_genre(rands[1]).genre_name
    genre3 = repo.get_genre(rands[2]).genre_name

    top_genre1 = get_movies_by_search(genre1, 'rating', repo)
    top_genre2 = get_movies_by_search(genre2, 'rating', repo)
    top_genre3 = get_movies_by_search(genre3, 'rating', repo)

    categories[1] = [latest_movies, 'Latest movies']
    categories[2] = [top_rated_movies, 'Top rated movies']
    categories[3] = [top_genre1, genre1]
    categories[4] = [top_genre2, genre2]
    categories[5] = [top_genre3, genre3]

    return categories

def get_user(username, repo):
    return repo.get_user(username)