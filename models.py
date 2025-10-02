

class User(UserMixin, db.Model):
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default = datetime.utcnow)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash  = db.Column(db.String(128))
    posts = db.relationship("Post", backref='autor', lazy='dynamic')
    followed = db.relationship(
        # "User", secondary=followers,
        # primaryjoin=(followers.c.follower_id == id),
        # secondaryjoin=(followers.c.followed_id == id),
        # backref=db.backref("followers", lazy="dynamic"), lazy="dynamic")