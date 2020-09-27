import CS235Flix.movies.services as services
from CS235Flix.domain.movie import Movie

def get_user(username, repo):
    return repo.get_user(username)

def update_movies(movies, repo):
    for i in range(len(movies)):
        movies[i] = movies[i].replace('<Movie ', '')
        movies[i] = movies[i].strip('>')
        movies[i] = movies[i].split(',')
        movies[i] = Movie(movies[i][0], int(movies[i][1]))
        movies[i] = repo.get_movie(movies[i])
    return movies