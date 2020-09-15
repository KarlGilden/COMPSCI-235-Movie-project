from flask import Flask, render_template
import os
import CS235Flix.adapters.repository as repo
from CS235Flix.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config=None):
    app = Flask(__name__)
    
    data_path = os.path.join('CS235Flix', 'datafiles')
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)
    @app.route('/')
    def index():
        return render_template('index.html', repo=repo.repo_instance)
    return app