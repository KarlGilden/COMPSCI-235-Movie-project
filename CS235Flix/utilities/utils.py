  
from flask import Blueprint, request, render_template, redirect, url_for, session

import CS235Flix.adapters.repository as repo
import CS235Flix.utilities.services as services

utilities_blueprint = Blueprint('utilities_bp', __name__)


def add_to_watchlist():
    movie = request.args.get('movie')
    username = session['username']
    user = services.get_user(username, repo.repo_instance)

    if user is None:
        return redirect('/authentication/login')
    
    user.watchlist.add_movie(movie)