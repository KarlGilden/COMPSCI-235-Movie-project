from flask import Blueprint, render_template, Flask, request, url_for, session, redirect
import CS235Flix.adapters.repository as repo
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, SubmitField, SelectField
import CS235Flix.utilities.utils as utilities 
import CS235Flix.movies.services as services
from CS235Flix.authentication.authentication import login_required
from CS235Flix.domain.movie import Movie
from wtforms.validators import DataRequired, Length, ValidationError


movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/browse', methods=['GET'])
def browse():
    form = SearchForm()
    movies_dict = services.get_movie_ids(repo.repo_instance)
    search_query = request.args.get('search')
        
    if search_query:
        movies = services.get_movies_by_search(search_query, repo.repo_instance)
    else:
        movies = services.get_latest_movies(repo.repo_instance)
        search_query = 'latest movies'

    return render_template(
        'browse_movies.html',
        movies=movies,
        form=form,
        search_query=search_query,
        movies_ids = movies_dict
    )



@movies_blueprint.route('/view-movie/<int:movie_id>', methods=['GET'])
def view_movie(movie_id):
    movie = services.create_movie(movie_id, repo.repo_instance)
    genres = ', '.join(movie.genres)
    actors = ', '.join(movie.actors)
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
    username = session['username']
    form = ReviewForm()
    movie_id = int(request.args.get('movie_id'))
    if form.is_submitted():
        print(movie_id)
        movie = services.get_movie_by_id(movie_id, repo.repo_instance)
        services.create_review(movie, form.review.data, form.rating.data, username)
        url = url_for('movies_bp.view_movie', movie_id=movie_id)
        return redirect(url) 

    return render_template(
        'new_review.html',
        form=form,
        movie=services.get_movie_by_id(movie_id, repo.repo_instance)
    )

    

class SearchForm(FlaskForm):
    search = StringField('search', _name='search', render_kw={"placeholder": "Search..."})

class ReviewForm(FlaskForm):
    review = TextAreaField('review', _name='review', render_kw={"placeholder": "Write your review here..."})
    movie_id = HiddenField('movie_id')
    rating = SelectField('rating', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int)
    submit = SubmitField('Submit')