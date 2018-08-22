# -*- coding: utf-8 -*-

from flask import request

from flask_jwt import jwt_required, current_identity

from backend.libs.bputils import create_api_blueprint
from backend.libs.decorators import query_params

bp = create_api_blueprint('user', __name__, url_prefix='user')


@bp.route('/', methods=['POST'])
def auth():
    """用户鉴权的API文档，该仅仅为了接口说明，无其他功能, 实际URL为/api/auth
    ---
    tags:
      - user
    parameters:
      - name:
        type: string
        required: true
        in: body
    responses:
      200:
        description: 如果鉴权成功，则返回JWT token
        scema:
          type: dict
        examples:
            {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MiwiaWF0IjoxNTM0MTU4NTMzLCJuYmYiOjE1MzQxNTg1MzMsImV4cCI6MTUzNDE4NzMzM30.9gbTK3rTwrIwrxE3bto2sB0NmX3XAOS98LNmS0dDiiQ"
            }
      401:
        description: 鉴权失败
    """
    args = request.json
    print(args)
    return


@bp.route('/', methods=['GET'])
@jwt_required()
def user():
    """获取用户详细信息
    ---
    tags:
      - user
    parameters:
      - name: Authorization
        in: header
        description: an jwt authorization header
        required: true
        type: string
    responses:
     200:
        description: 返回用户信息
        examples:
            {
                "code": 200,
                "msg": "success",
                "data": {
                    "name": "guoming",
                    "phone": "13301383954",
                    "id": 2
                    }
            }

    """
    c = current_identity
    return dict(id=c.id, phone=c.phone, name=c.name)
