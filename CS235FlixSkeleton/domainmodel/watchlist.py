from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self._movies = list()

    @property
    def movies(self):
        return self._movies

    @movies.setter
    def movies(self, movies):
        self._movies = movies

    def add_movie(self, movie: Movie):
        if movie not in self._movies:
            self._movies.append(movie)
    
    def remove_movie(self, movie: Movie):
        if movie in self._movies:
            self._movies.remove(movie)

    def select_movie_to_watch(self, index):
        if index >= len(self._movies):
            return None
        return self._movies[index]

    def size(self):
        return len(self._movies)
    
    def first_movie_in_watchlist(self):
        if len(self._movies) != 0:
            return self._movies[0]
        else:
            return None
    
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count <= len(self._movies):
            self.count += 1
        else:
            raise StopIteration
        

