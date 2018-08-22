# -*- coding: utf-8 -*-
"""教练model
"""

from backend.client import db
from backend.libs.model import BaseModelMixin


class Coach(BaseModelMixin):
    """教练model
    """
    # 名称
    name = db.Column(db.String(50), info=dict(creatable=False, editable=True))
    # 年龄
    age = db.Column(db.Integer, info=dict(creatable=False, editable=True))
    # 性别
    sex = db.Column(db.Integer, info=dict(creatable=False, editable=True))
    # 教练评分
    score = db.Column(db.Float, info=dict(creatable=False, editable=True))
    # 教练描述
    desc = db.Column(db.Text, info=dict(creatable=False, editable=True))
    # 国籍
    country = db.Column(
        db.String(100), info=dict(creatable=False, editable=True))
    # 资格证书，json格式存储[xx,xx]
    q_certificate = db.Column(
        db.Text, info=dict(creatable=False, editable=True))
    # 可授课程
    courses = db.Column(db.Text, info=dict(creatable=False, editable=True))
    # 教练介绍视频链接
    intro_ls = db.Column(db.Text, info=dict(creatable=False, editable=True))
    # vipfit评语
    vipfit_desc = db.Column(
        db.String(2045), info=dict(creatable=False, editable=True))
