from flask import request, jsonify, Response
from flask_restx import Resource, Namespace, abort

from api.models import JobNotice, JobOpen, JobHunt
from api.route.auth import login_required

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

    # @login_required
    # def post(self):
@post.route("/jobnotice/<int:id>")
class Detail(Resource):
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

# 구인게시판
@post.route("/jobopen/")
class _JobNotice(Resource):
    @login_required
    def get(self):
        jobOpen_list = JobOpen.query.order_by(JobNotice.create_date.desc())
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

    # @login_required
    # def post(self):
@post.route("/jobopen/<int:id>")
class Detail(Resource):
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

# 구직게시판
@post.route("/jobhunt/")
class _JobNotice(Resource):
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

    # @login_required
    # def post(self):
@post.route("/jobhunt/<int:id>")
class Detail(Resource):
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
