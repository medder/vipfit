# -*- coding: utf-8 -*-
"""用户model
"""

from werkzeug.security import safe_str_cmp

from backend.client import db
from backend.libs.model import BaseModelMixin


def authenticate(phone, password):
    """前端传入的参数格式必须是:
    POST /api/auth HTTP/1.1
    Content-Type: application/json

    {
        "phone": "xx",
        "password": "pass"
    }
    其中, phone 需要在config中配置, 在此项目中配置为phone
    """
    user = User.query.filter_by(phone=phone).first()
    if user and safe_str_cmp(
            user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()


class User(BaseModelMixin):
    """用户model
    """
    # 手机号码
    phone = db.Column(db.String(11), info=dict(creatable=True, editable=False))
    # 密码
    password = db.Column(
        db.String(64), info=dict(creatable=True, editable=True))
    # 用户名称
    name = db.Column(db.String(50), info=dict(creatable=True, editable=True))
