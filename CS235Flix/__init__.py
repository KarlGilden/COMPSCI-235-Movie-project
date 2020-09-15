from flask import Flask, render_template
import os
import CS235Flix.adapters.repository as repo
from CS235Flix.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config=None):
    app = Flask(__name__)
    
    data_path = os.path.join('CS235Flix', 'datafiles')
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

    return app