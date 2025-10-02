from flask import Flask
from app.models import User

from app import db

app = Flask(__name__)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    app.run(debug=True)

