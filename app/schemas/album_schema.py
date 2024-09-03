from app.extensions import ma
from app.models.album import Album


class AlbumSchema(ma.SQLAlchemyAutoSchema):
    model = Album
    load_instance = True


album_schema = AlbumSchema()
albums_schema = AlbumSchema(many=True)
