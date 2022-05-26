from api import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable =False)
    created = db.Column(db.DateTime(), nullable=False)
    updated = db.Column(db.DateTime(), nullable=False)

class JobNotice(db.Model): # 취업게시글
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    update_date = db.Column(db.DateTime(), nullable=False)
    user_name = db.Column(db.Integer, db.ForeignKey('user.username', ondelete='CASCADE'), nullable=False)
    user = db.relationship("User", backref=db.backref("job_notice_set"))

class JobOpen(db.Model): # 구인게시글
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    update_date = db.Column(db.DateTime(), nullable=False)
    user_name = db.Column(db.Integer, db.ForeignKey('user.username', ondelete='CASCADE'), nullable=False)
    user = db.relationship("User", backref=db.backref("job_open_set"))

class JobHunt(db.Model): # 구직게시글
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    update_date = db.Column(db.DateTime(), nullable=False)
    user_name = db.Column(db.Integer, db.ForeignKey('user.username', ondelete='CASCADE'), nullable=False)
    user = db.relationship("User", backref=db.backref("job_hunt_set"))