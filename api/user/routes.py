from flask import Blueprint, request, jsonify
from api.user.Schema import UserSchema
from api.user.model import User
from api import db

user = Blueprint('user', __name__)


@user.route("/user/register", methods=['POST'])
def register():
    # error list to return
    error = []

    # create schema
    user_schema = UserSchema()
    users_schema = UserSchema(many=True)

    # get user data to register
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    # check if data are null?
    if username == "" or email == "" or password == "":
        error.append("The inputs can't be empty")

    # validation
    existed_username = User.query.filter_by(username=username).first()
    existed_email = User.query.filter_by(email=email).first()
    if existed_username:
        error.append("Username already existed.Please use another one.")
    if existed_email:
        error.append("Email already existed.Please use another one.")

    if not error:
        # add to database
        add_user = User(username=username, email=email, password=password)
        db.session.add(add_user)
        db.session.commit()
        return user_schema.jsonify(add_user)
    else:
        return jsonify({"error": error})
