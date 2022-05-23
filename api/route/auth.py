from flask import flash, request, session, g, jsonify
from flask_restx import Resource, Namespace, abort
from werkzeug.security import generate_password_hash, check_password_hash

from api import db
from api.models import User

auth = Namespace('auth')

@auth.route('/signup/')
class Signup(Resource):
    def post(self):
        user = User.query.filter_by(user_id=request.form['user_id']).first()
        if not user:
            user = User(user_id=request.form['user_id'],
                        password=generate_password_hash(request.form['password']),
                        email=request.form['email'])
            db.session.add(user)
            db.session.commit()
            return jsonify({"message":"회원가입에 성공하셨습니다."})
        else:
            abort(409, message="이미 존재하는 사용자입니다.")

@auth.route('/login/')
class Login(Resource):
    def post(self):
        error = None
        user = User.query.filter_by(user_id=request.form['user_id']).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, request.form['password']):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return jsonify({"message":"로그인에 성공하셨습니다."})
        abort(404, message=error)