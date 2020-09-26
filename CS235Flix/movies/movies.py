from flask import Blueprint, render_template, Flask, request, url_for, session, redirect
import CS235Flix.adapters.repository as repo
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, SubmitField, SelectField, BooleanField, RadioField
import CS235Flix.utilities.utils as utilities 
import CS235Flix.movies.services as services
from CS235Flix.authentication.authentication import login_required
from CS235Flix.domain.movie import Movie
from wtforms.validators import DataRequired, Length, ValidationError

movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/browse', methods=['GET'])
def browse():
    # define form
    form = SearchForm()
    # get search settings
    search_query = request.args.get('search')
    setting = request.args.get('search_settings')
    
    # get list of movies to display according to settings
    if form.validate_on_submit:
        if search_query == None and setting == None:
            setting = 'most recent'
        movies = services.get_movies_by_search(search_query, setting, repo.repo_instance)

    # render page
    return render_template(
        'browse_movies.html',
        movies=movies,
        form=form,
        type=type(movies) == list,
        search_query=search_query,
        setting=setting
    )



@movies_blueprint.route('/view-movie/<int:movie_id>', methods=['GET'])
def view_movie(movie_id):
    # get movie to display by id
    movie = services.create_movie(movie_id, repo.repo_instance)

    # create genre and actor strings for better display
    genres = ', '.join(movie.genres)
    actors = ', '.join(movie.actors)

    # render template
    return render_template(
        'movie_preview.html',
        movie=movie,
        genres=genres,
        actors=actors,
        review_url=url_for('movies_bp.add_review', movie_id=movie_id)
        )

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