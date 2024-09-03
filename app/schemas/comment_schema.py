from app.extensions import ma
from app.models.comment import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    model = Comment
    load_instance = True


user_schema = CommentSchema()
users_schema = CommentSchema(many=True)
