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
    """用户model, 通过动态密码登录
    """
    # 手机号码
    phone = db.Column(db.String(11), info=dict(creatable=True, editable=False))
    # 用户名称
    name = db.Column(db.String(50), info=dict(creatable=False, editable=True))
    # 性别
    sex = db.Column(db.Integer, info=dict(creatable=False, editable=True))
    # 生日
    birth_date = db.Column(
        db.DateTime, info=dict(creatable=False, editable=True))
    # 所在城市
    city = db.Column(db.String(50), info=dict(creatable=False, editable=True))
    # 头像img地址
    head_img = db.Column(
        db.String(1024), info=dict(creatable=False, editable=True))
    # 微信唯一用户标识
    openid = db.Column(
        db.String(64), info=dict(creatable=False, editable=True))

    # 收货地址信息
    # 收货人名称
    ems_name = db.Column(
        db.String(50), info=dict(creatable=False, editable=True))
    # 收货人性别
    ems_sex = db.Column(db.Integer, info=dict(creatable=False, editable=True))
    # 收货人电话号码
    ems_phone = db.Column(
        db.String(11), info=dict(creatable=False, editable=True))
    # 收货人地址
    ems_address = db.Column(
        db.String(255), info=dict(creatable=False, editable=True))
    # 收货人楼号门牌
    ems_bnumber = db.Column(
        db.String(100), info=dict(creatable=False, editable=True))
