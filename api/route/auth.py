from flask import request, jsonify, Response
from flask_restx import Resource, Namespace, abort

from api import db
from api.models import User

import bcrypt, jwt
from config import JWT_SECRET_KEY

auth = Namespace('auth')

@auth.route('')
class CheckToken(Resource):
    def post(self):
        token = request.headers.get('authorization')

        if token is not None:
            try:
                payload = jwt.decode(token, JWT_SECRET_KEY, "HS256")
            except jwt.InvalidTokenError:
                payload = None
            if payload is not None:
                return # 추가될 예정.
            else:
                abort(401, message="토큰 검증에 실패하셨습니다.")
        else:
            abort(401, message="토큰 검증에 실패하셨습니다.")



@auth.route('/signup/')
class Signup(Resource):
    def post(self):
        user = User.query.filter((User.username==request.json["username"])|(User.email==request.json['email'])).first()
        if not user:
            username = request.json['username']
            password = bcrypt.hashpw(request.json['password'].encode("utf-8"), bcrypt.gensalt())
            email = request.json['email']
            user = User(username=username,
                        password=password,
                        email=email)

            db.session.add(user)
            db.session.commit()

            return jsonify({
                'message': "회원가입에 성공하셨습니다."
            })
        else:
            abort(409, message="이미 존재하는 사용자입니다.")

@auth.route('/login/')
class Login(Resource):
    def post(self):
        error = None
        user = User.query.filter_by(username=request.json['username']).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not bcrypt.checkpw(request.json['password'].encode('utf-8'), user.password):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            payload = {
                "username": user.username,
                "password": user.password.decode("utf-8")
            }
            token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
            response = Response()
            response.headers['authorization'] = token
            return response
        abort(403, message=error)