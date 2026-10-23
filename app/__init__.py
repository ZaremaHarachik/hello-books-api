

from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import books_bp
import os


# Create the Flask application
def create_app(config=None):
    app = Flask(__name__)

    # Configure the Flask app with SQLAlchemy settings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI'
    )

    if config:
        app.config.update(config)

    # Configure the database and migration instances with the Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app
