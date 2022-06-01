from flask import request, jsonify, Response, json
from flask_restx import Resource, Namespace, abort

from api import db
from api.models import User

import bcrypt, jwt
from config import JWT_SECRET_KEY
from functools import wraps
from datetime import datetime

auth = Namespace('auth')

@auth.route('/signup/')
class Signup(Resource):
    def post(self):
        user = User.query.filter((User.username==request.json["username"])|(User.email==request.json['email'])).first()
        if not user:
            username = request.json['username']
            password = bcrypt.hashpw(request.json['password'].encode("utf-8"), bcrypt.gensalt())
            email = request.json['email']
            user = User(username=username,
                        password=password.decode('utf-8'),
                        email=email,
                        created= datetime.now(),
                        updated= datetime.now())

            db.session.add(user)
            db.session.commit()
            db.session.remove()
            return jsonify({
                'code': 1,
                'msg' : "회원가입 성공!",
                'data':{}
            })
        else:
            return jsonify({
                'code': -1,
                'msg': "회원가입 실패!",
                'data': {}
            })

@auth.route('/login/')
class Login(Resource):
    def post(self):
        error = None
        user = User.query.filter_by(username=request.json['username']).first()

        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not bcrypt.checkpw(request.json['password'].encode('utf-8'), user.password.encode('utf-8')):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            payload = {
                "username": user.username,
                "password": user.password
            }
            token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
            print(token)
            body = json.dumps({
                "code": 1,
                "msg": "로그인에 성공하셨습니다.",
                "data": {
                    "id" : user.id,
                    "username" : user.username,
                    "password": user.password,
                    "email": user.email,
                    "created" : user.created.strftime('%Y-%m-%d'),
                    "updated" : user.updated.strftime('%Y-%m-%d')
                }
            }, ensure_ascii=False)
            db.session.remove()
            response = Response(body)
            response.headers['authorization'] = token
            return response
        return jsonify({
            "code": -1,
            "msg": error,
            "data": {}
        })


# 토큰 검증을 위한 함수들
def check_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, "HS256")
    except jwt.InvalidTokenError:
        payload = None
    return payload

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwagrs):
        token = request.headers.get('authorization')
        if token is not None:
            payload = check_token(token)
            if payload is None:
                abort(401, message="토큰 검증에 실패하셨습니다.")
        else:
            abort(401, message="토큰 검증에 실패하셨습니다.")
        return f(*args, **kwagrs)
    return decorated_function