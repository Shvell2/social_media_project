from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from flask_login import UserMixin
from app import login


friends_table = db.Table("friends",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("friend_id", db.Integer, db.ForeignKey("user.id")))

class User(UserMixin, db.Model):
    about_me = db.Column(db.String(140))
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    friends = db.relationship("User", secondary = friends_table, backref="friend", primaryjoin = (friends_table.c.user_id == id), secondaryjoin = (friends_table.c.friend_id == id))
    # def __repr__(self):
    #     return 'User {}'.format(self.username)

    def set_password(self, password):
        print(password)
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print(self.password_hash, password)
        return check_password_hash(self.password_hash, password)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))

