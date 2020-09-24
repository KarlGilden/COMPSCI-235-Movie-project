from flask import Flask
import os
import CS235Flix.adapters.repository as repo
from CS235Flix.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = os.path.join('CS235Flix', 'datafiles')
    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    return app