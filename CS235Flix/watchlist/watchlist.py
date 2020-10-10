from flask import Blueprint, render_template, Flask, request, url_for, session, redirect
import CS235Flix.adapters.repository as repo
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, SubmitField, SelectField, BooleanField, RadioField
import CS235Flix.movies.services as services
import CS235Flix.watchlist.services as watchlist_services
from CS235Flix.authentication.authentication import login_required
from CS235Flix.domain.movie import Movie
from wtforms.validators import DataRequired, Length, ValidationError
from CS235Flix.domain.watchlist import WatchList

watchlist_blueprint = Blueprint('watchlist_bp', __name__, url_prefix='/watchlist')

@watchlist_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def watchlist():
    form= WatchlistForm()
    # get user and authenticate
    username = session['username']
    user = services.get_user(username, repo.repo_instance)
    if user is None:
        return redirect('/authentication/login')

    # get user's watchlist
    watchlist = user.watchlist
    movies = watchlist.movies
    if watchlist.size() == 0:
        movies = 'Nothing to see here'



    # render template
    return render_template(
        'watchlist.html',
        username=username,
        movies=movies,
        type=type(movies) == list,
        form=form
        )

@watchlist_blueprint.route('/success', methods=['GET', 'POST'])
def success():
    # get user
    username = session['username']
    user = services.get_user(username, repo.repo_instance)

    # get movie
    movie_id = int(request.args.get('movie_id'))
    movie = services.get_movie_by_id(movie_id, repo.repo_instance) # get movie by id

    # remove movie
    user.watchlist.remove_movie(movie)

    # redirect to watchlist
    return redirect(url_for('watchlist_bp.watchlist'))


class WatchlistForm(FlaskForm):
    movie = HiddenField('movie_id')