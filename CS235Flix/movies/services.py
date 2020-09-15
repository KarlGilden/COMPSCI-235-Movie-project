from CS235Flix.adapters.repository import AbstractRepository

def get_movies_by_actor(actor, repo):
    movies = repo.get_movies_by_actor(actor)
    return movies