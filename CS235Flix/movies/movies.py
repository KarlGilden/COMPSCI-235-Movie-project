from flask import Blueprint, render_template
import CS235Flix.adapters.repository as repo

import CS235Flix.movies.services as services


movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies():
    movies = services.get_movies_by_actor('Chris Pratt', repo.repo_instance)
    return render_template(
        'browse_movies.html',
        movies=movies
    )