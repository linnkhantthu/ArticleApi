from api import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username', 'email')
