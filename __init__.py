from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models import user, post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': user.User, 'Post': post.Post}