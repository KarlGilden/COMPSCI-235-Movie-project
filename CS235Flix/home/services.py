from CS235Flix.adapters.repository import AbstractRepository

def get_movies_by_rank(repo):
    movies = repo.get_movies_by_rating()
    return movies