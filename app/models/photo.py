from app.extensions import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    thumbnailUrl = db.Column(db.String(255), nullable=True)
    liked = db.Column(db.Boolean, default=False)
    numberOfLike = db.Column(db.Integer, default=0)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    def __init__(self, title, url, thumbnailUrl, liked, numberOfLike, album_id):
        self.title = title
        self.url = url
        self.thumbnailUrl = thumbnailUrl
        self.liked = liked
        self.numberOfLike = numberOfLike
        self.album_id = album_id

    def __repr__(self):
        return f'<Photo {self.title}>'
