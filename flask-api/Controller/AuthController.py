from flask import request, jsonify, current_app as app
from Model.UserModel import User
from Model import db
from Controller.BaseController import BaseController
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
import uuid


class AuthController(BaseController):
    @staticmethod
    def login():
        # creates dictionary of form data
        auth = request.form
    
        if not auth or not auth.get('email') or not auth.get('password'):
            # returns 401 if any email or / and password is missing
            return jsonify({'message' : 'Could not verify'}), 401
    
        user = User.query\
            .filter_by(email = auth.get('email'))\
            .first()
    
        if not user:
            # returns 401 if user does not exist
            return jsonify({'message' : 'Could not verify'}), 401
    
        if check_password_hash(user.password, auth.get('password')):
            # generates the JWT Token
            token = jwt.encode({
                'public_id': user.public_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, app.config['SECRET_KEY'])
    
            return jsonify({'token' : token.decode('UTF-8')})
        # returns 403 if password is wrong
        return jsonify({'message' : 'Could not verify'}), 403
    
    @staticmethod
    def register():
        # creates a dictionary of the form data
        data = request.form
    
        # gets name, email and password
        name, email = data.get('name'), data.get('email')
        password = data.get('password')
    
        # checking for existing user
        user = User.query\
            .filter_by(email = email)\
            .first()
        if not user:
            # database ORM object
            user = User(
                public_id = str(uuid.uuid4()),
                name = name,
                email = email,
                password = generate_password_hash(password)
            )
            # insert user
            db.session.add(user)
            db.session.commit()
    
            return jsonify({'message' : 'New user created!'})
        else:
            # returns 202 if user already exists
            return jsonify({'message' : 'User already exists. Please Log in.'}), 202