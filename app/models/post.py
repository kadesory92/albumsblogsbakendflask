from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    liked = db.Column(db.Boolean, default=False)
    numberOfLike = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __init__(self, title, content, liked, numberOfLike, user_id):
        self.title = title
        self.content = content
        self.liked = liked
        self.numberOfLike = numberOfLike
        self.user_id = user_id

    def __repr__(self):
        return f'<Post {self.title}>'
