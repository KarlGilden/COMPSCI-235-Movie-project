from flask import Blueprint, render_template, request, session
import CS235Flix.adapters.repository as repo
import CS235Flix.home.services as services
import CS235Flix.utilities.utils as utilities
from CS235Flix.movies.movies import SearchForm
home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    topmovies = services.get_movies_by_rank(repo.repo_instance)
    
    return render_template(
        'home.html',
        movies=topmovies
        
    )