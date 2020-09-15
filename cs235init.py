from flask import Flask, render_template, url_for
from CS235Flix import create_app
import csv

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)