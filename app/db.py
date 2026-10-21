
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base


# Initialize SQLAlchemy and Migrate instances
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
