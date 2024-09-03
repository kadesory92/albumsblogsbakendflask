from app.extensions import ma
from app.models.photo import Photo


class PhotoSchema(ma.SQLAlchemyAutoSchema):
    model = Photo
    load_instance = True


photo_schema = PhotoSchema()
photos_schema = PhotoSchema(many=True)
