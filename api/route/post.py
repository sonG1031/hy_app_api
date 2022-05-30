from flask import request, jsonify
from flask_restx import Resource, Namespace
from api.models import JobNotice, JobOpen, JobHunt
from api.route.auth import login_required
from api import db
from datetime import datetime

post = Namespace("post")


# 취업게시판
@post.route("/jobnotice/")
class _JobNotice(Resource):
    @login_required
    def get(self):
        jobNotice_list = JobNotice.query.order_by(JobNotice.create_date.desc())
        lst = []

        code = 1
        if jobNotice_list is None:
            code = -1
        else:
            lst = get_infoList(jobNotice_list)

        return jsonify({
            "code" : code,
            "msg" : "취업게시판 목록 불러오기 완료",
            "data": lst
        })
    @login_required
    def post(self):
        job_notice = JobNotice(title=request.json['title'],content=request.json['content'], create_date=datetime.now(),
                               update_date=datetime.now(), user_name=request.json['username'])
        db.session.add(job_notice)
        db.session.commit()
        return jsonify({
            "code" : 1,
            "msg" : "글쓰기완료",
            "data" : {
                "id" : job_notice.id,
                "title" : job_notice.title,
                "content" : job_notice.content,
                "user" : {
                    "id" : job_notice.user.id,
                    "username" : job_notice.user.username,
                    "password" : job_notice.user.password.decode("utf-8"),
                    "email" : job_notice.user.email,
                    "created" : job_notice.user.created.strftime('%Y-%m-%d'),
                    "updated" : job_notice.user.updated.strftime('%Y-%m-%d')
                },
                "created" : job_notice.create_date.strftime('%Y-%m-%d'),
                "updated" : job_notice.update_date.strftime('%Y-%m-%d')
            }
        })


@post.route("/jobnotice/<int:id>")
class JobNoDetail(Resource):
    @login_required
    def get(self, id):
        job_notice = JobNotice.query.get_or_404(id)
        data = {}

        code = 1
        if job_notice is None:
            code = -1
        else:
            data = get_info(job_notice)

        return jsonify({
            "code": code,
            "msg": "취업게시판 상세보기 완료",
            "data" : data
        })

    @login_required
    def put(self, id):
        job_notice = JobNotice.query.get_or_404(id)
        job_notice.title = request.json["title"]
        job_notice.content = request.json["content"]
        job_notice.update_date = datetime.now()

        db.session.commit()
        return jsonify({
            "code" : 1,
            "msg" : "수정하기완료",
            "data" : {
                "id" : job_notice.id,
                "title" : job_notice.title,
                "content" : job_notice.content,
                "user" : {
                    "id" : job_notice.user.id,
                    "username" : job_notice.user.username,
                    "password" : job_notice.user.password.decode("utf-8"),
                    "created" : job_notice.user.created.strftime('%Y-%m-%d'),
                    "updated" : job_notice.user.updated.strftime('%Y-%m-%d')
                },
                "created" : job_notice.create_date.strftime('%Y-%m-%d'),
                "updated" : job_notice.update_date.strftime('%Y-%m-%d')
            }
        })

    @login_required
    def delete(self, id):
        job_notice = JobNotice.query.get_or_404(id)
        db.session.delete(job_notice)
        db.session.commit()
        return jsonify({
            "code" : 1,
            "msg" : "삭제하기완료",
            "data" : "null"
        })


# 구인게시판
@post.route("/jobopen/")
class _JobOpen(Resource):
    @login_required
    def get(self):
        jobOpen_list = JobOpen.query.order_by(JobOpen.create_date.desc())
        lst = []

        code = 1
        if jobOpen_list is None:
            code = -1
        else:
            lst = get_infoList(jobOpen_list)

        return jsonify({
            "code" : code,
            "msg" : "구인게시판 목록 불러오기 완료",
            "data": lst
        })

    @login_required
    def post(self):
        job_open = JobOpen(title=request.json['title'], content=request.json['content'], create_date=datetime.now(),
                               update_date=datetime.now(), user_name=request.json['username'])
        db.session.add(job_open)
        db.session.commit()
        return jsonify({
            "code": 1,
            "msg": "글쓰기완료",
            "data": {
                "id": job_open.id,
                "title": job_open.title,
                "content": job_open.content,
                "user": {
                    "id": job_open.user.id,
                    "username": job_open.user.username,
                    "password": job_open.user.password.decode("utf-8"),
                    "email": job_open.user.email,
                    "created": job_open.user.created.strftime('%Y-%m-%d'),
                    "updated": job_open.user.updated.strftime('%Y-%m-%d')
                },
                "created": job_open.create_date.strftime('%Y-%m-%d'),
                "updated": job_open.update_date.strftime('%Y-%m-%d')
            }
        })


@post.route("/jobopen/<int:id>")
class JobOpDetail(Resource):
    @login_required
    def get(self, id):
        job_open = JobOpen.query.get_or_404(id)
        data = {}

        code = 1
        if job_open is None:
            code = -1
        else:
            data = get_info(job_open)

        return jsonify({
            "code": code,
            "msg": "구인게시판 상세보기 완료",
            "data" : data
        })

    @login_required
    def put(self, id):
        job_open = JobOpen.query.get_or_404(id)
        job_open.title = request.json["title"]
        job_open.content = request.json["content"]
        job_open.update_date = datetime.now()

        db.session.commit()
        return jsonify({
            "code": 1,
            "msg": "수정하기완료",
            "data": {
                "id": job_open.id,
                "title": job_open.title,
                "content": job_open.content,
                "user": {
                    "id": job_open.user.id,
                    "username": job_open.user.username,
                    "password": job_open.user.password.decode("utf-8"),
                    "created": job_open.user.created.strftime('%Y-%m-%d'),
                    "updated": job_open.user.updated.strftime('%Y-%m-%d')
                },
                "created": job_open.create_date.strftime('%Y-%m-%d'),
                "updated": job_open.update_date.strftime('%Y-%m-%d')
            }
        })

    @login_required
    def delete(self, id):
        job_open = JobOpen.query.get_or_404(id)
        db.session.delete(job_open)
        db.session.commit()
        return jsonify({
            "code" : 1,
            "msg" : "삭제하기완료",
            "data" : "null"
        })


# 구직게시판
@post.route("/jobhunt/")
class _JobHunt(Resource):
    @login_required
    def get(self):
        jobHunt_list = JobHunt.query.order_by(JobHunt.create_date.desc())
        lst = []

        code = 1
        if jobHunt_list is None:
            code = -1
        else:
            lst = get_infoList(jobHunt_list)

        return jsonify({
            "code" : code,
            "msg" : "구직게시판 목록 불러오기 완료",
            "data": lst
        })

    @login_required
    def post(self):
        job_hunt = JobHunt(title=request.json['title'], content=request.json['content'], create_date=datetime.now(),
                           update_date=datetime.now(), user_name=request.json['username'])
        db.session.add(job_hunt)
        db.session.commit()
        return jsonify({
            "code": 1,
            "msg": "글쓰기완료",
            "data": {
                "id": job_hunt.id,
                "title": job_hunt.title,
                "content": job_hunt.content,
                "user": {
                    "id": job_hunt.user.id,
                    "username": job_hunt.user.username,
                    "password": job_hunt.user.password.decode("utf-8"),
                    "email": job_hunt.user.email,
                    "created": job_hunt.user.created.strftime('%Y-%m-%d'),
                    "updated": job_hunt.user.updated.strftime('%Y-%m-%d')
                },
                "created": job_hunt.create_date.strftime('%Y-%m-%d'),
                "updated": job_hunt.update_date.strftime('%Y-%m-%d')
            }
        })


@post.route("/jobhunt/<int:id>")
class JobHuntDetail(Resource):
    @login_required
    def get(self, id):
        job_hunt = JobHunt.query.get_or_404(id)
        data = {}

        code = 1
        if job_hunt is None:
            code = -1
        else:
            data = get_info(job_hunt)

        return jsonify({
            "code": code,
            "msg": "구직게시판 상세보기 완료",
            "data" : data
        })

    @login_required
    def put(self, id):
        job_hunt = JobHunt.query.get_or_404(id)
        job_hunt.title = request.json["title"]
        job_hunt.content = request.json["content"]
        job_hunt.update_date = datetime.now()

        db.session.commit()
        return jsonify({
            "code": 1,
            "msg": "수정하기완료",
            "data": {
                "id": job_hunt.id,
                "title": job_hunt.title,
                "content": job_hunt.content,
                "user": {
                    "id": job_hunt.user.id,
                    "username": job_hunt.user.username,
                    "password": job_hunt.user.password.decode("utf-8"),
                    "created": job_hunt.user.created.strftime('%Y-%m-%d'),
                    "updated": job_hunt.user.updated.strftime('%Y-%m-%d')
                },
                "created": job_hunt.create_date.strftime('%Y-%m-%d'),
                "updated": job_hunt.update_date.strftime('%Y-%m-%d')
            }
        })

    @login_required
    def delete(self, id):
        job_hunt = JobHunt.query.get_or_404(id)
        db.session.delete(job_hunt)
        db.session.commit()
        return jsonify({
            "code" : 1,
            "msg" : "삭제하기완료",
            "data" : "null"
        })

# json 직렬화를 위한 함수들
def get_infoList(info_list):
    lst = []
    for info in info_list:
        lst.append(
            {
                "id": info.id,
                "title": info.title,
                "content": info.content,
                "created": info.create_date.strftime('%Y-%m-%d'),
                "updated": info.update_date.strftime('%Y-%m-%d'),
                "user": {
                    "id": info.user.id,
                    "username": info.user.username,
                    "password": info.user.password.decode("UTF-8"),
                    "email": info.user.email,
                    "created": info.user.created.strftime('%Y-%m-%d'),
                    "updated": info.user.updated.strftime('%Y-%m-%d')
                }
            }
        )
    return lst
def get_info(info):
    data = {
        "id": info.id,
        "title": info.title,
        "content": info.content,
        "created": info.create_date.strftime('%Y-%m-%d'),
        "updated": info.update_date.strftime('%Y-%m-%d'),
        "user": {
            "id": info.user.id,
            "username": info.user.username,
            "password": info.user.password.decode("UTF-8"),
            "email": info.user.email,
            "created": info.user.created.strftime('%Y-%m-%d'),
            "updated": info.user.updated.strftime('%Y-%m-%d')
        }
    }
    return data
