from flask import Blueprint, render_template, Flask, request, url_for, session, redirect
import CS235Flix.adapters.repository as repo
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, SubmitField, SelectField, BooleanField, RadioField
import CS235Flix.utilities.utils as utilities 
import CS235Flix.movies.services as services
from CS235Flix.authentication.authentication import login_required
from CS235Flix.domain.movie import Movie
from wtforms.validators import DataRequired, Length, ValidationError

movies_blueprint = Blueprint('movies_bp', __name__, url_prefix='/movies')

@movies_blueprint.route('/browse', methods=['GET', 'POST'])
def browse():
    watchlist = []
    try:
        user = session['username']
        user = services.get_user(user, repo.repo_instance)
        watchlist = user.watchlist
        watchlist = watchlist.movies
    except:
        pass

    # define form
    form = SearchForm()

    # set home browse page categories
    categories = services.create_browse_categories(repo.repo_instance)

    # get list of movies to display according to settings and redirect to results page
    if request.method == 'POST':
        setting = form.search_settings.data
        search_query = form.search.data
        return redirect(url_for('movies_bp.results', page=0, setting=setting, search=search_query))

    # render page
    return render_template(
        'browse_movies.html',
        categories=categories,
        form=form,
        watchlist=watchlist
    )

@movies_blueprint.route('/browse/results', methods=['GET', 'POST'])
def results():
    search_query = request.args.get('search')
    setting = request.args.get('setting')
    page = int(request.args.get('page'))
    
    movies_per_page = 28
    movies = services.get_movies_by_search(search_query, setting, repo.repo_instance)
    numpages = len(movies) // movies_per_page
    movies = list(services.split_pages(movies, movies_per_page))

    return render_template(
        'browse_results.html',
        movies=movies,
        type=type(movies) == list,
        page=page,
        numpages=numpages,
        search_query=search_query,
        setting=setting
    )


@movies_blueprint.route('/view-movie/<int:movie_id>', methods=['GET', 'POST'])
def view_movie(movie_id):
    form = WatchlistForm()
    # get movie to display by id
    movie = services.create_movie(movie_id, repo.repo_instance)
    in_watchlist = False
    try:
        user = session['username']
        user = services.get_user(user, repo.repo_instance)
        watchlist = user.watchlist
        if movie in watchlist.movies:
            in_watchlist = True
    except:
        pass

    if request.method == 'POST':
        return redirect(url_for('movies_bp.success', movie_id=movie_id))
    # create genre and actor strings for better display
    genres = ', '.join(movie.genres)
    actors = ', '.join(movie.actors)

    # render template
    return render_template(
        'movie_preview.html',
        movie=movie,
        genres=genres,
        actors=actors,
        review_url=url_for('movies_bp.add_review', movie_id=movie_id),
        form=form,
        in_watchlist=in_watchlist
        )


@movies_blueprint.route('/view-movie/<int:movie_id>/success', methods=['GET'])
@login_required
def success(movie_id):
    username = session['username']
    user = services.get_user(username, repo.repo_instance)

    if user is None:
        return redirect('/authentication/login')

    movie = services.get_movie_by_id(movie_id, repo.repo_instance) # get movie by id
    user.watchlist.add_movie(movie)

    return redirect(url_for('movies_bp.view_movie', movie_id=movie_id))


@movies_blueprint.route('/add-review', methods=['GET', 'POST'])
@login_required
def add_review():
    # get session username and review form
    username = session['username']
    form = ReviewForm()

    # get movie_id
    movie_id = int(request.args.get('movie_id'))

    # create review from review form and redirect to movie page
    if form.is_submitted():
        movie = services.get_movie_by_id(movie_id, repo.repo_instance) # get movie by id
        services.create_review(movie, form.review.data, form.rating.data, username) # create review
        return redirect(url_for('movies_bp.view_movie', movie_id=movie_id)) # redirect to movie page

    # render template
    return render_template(
        'new_review.html',
        form=form,
        movie=services.get_movie_by_id(movie_id, repo.repo_instance)
    )

    
# form definitions 
class SearchForm(FlaskForm):
    search_settings = RadioField('radio', choices=[('A-Z', 'A-Z'), ('most recent', 'Most recent'), ('oldest', 'Oldest')])
    search = StringField(
        'search',
        _name='search',
        render_kw={"placeholder": "Search for Actor, Director, Genre etc..."}
        )

class ReviewForm(FlaskForm):
    review = TextAreaField('review', _name='review', render_kw={"placeholder": "Write your review here..."})
    movie_id = HiddenField('movie_id')
    rating = SelectField('rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int)
    submit = SubmitField('Submit')

class WatchlistForm(FlaskForm):
    movie = HiddenField('movie_id')