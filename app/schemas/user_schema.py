from app.extensions import ma
from app.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    model = User
    exclude = ('password', )
    load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)
