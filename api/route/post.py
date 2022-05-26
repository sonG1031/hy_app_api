from flask import request, jsonify, Response
from flask_restx import Resource, Namespace, abort

from api.models import JobNotice, JobOpen, JobHunt

post = Namespace("post")

@post.route("/jobnotice/")
class JobNotice(Resource):
    def get(self):
        jobNotice_list = JobNotice.query.order_by(JobNotice.create_date.desc())
        return jsonify({"data": jobNotice_list})