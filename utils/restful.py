from flask import jsonify


class HttpCode(object):
    ok = 200
    uautherror = 400
    paramserror = 401
    servererror = 500


def restful_result(code, message, data):
    return jsonify({
        "code": code,
        "message": message,
        "data": data or {}
    })


def success(message="", data=None):
    return restful_result(
        code=HttpCode.ok,
        message=message,
        data=data
    )


def uauth_error(message=""):
    return restful_result(
        code=HttpCode.uautherror,
        message=message,
        data=None
    )


def params_error(message=""):
    return restful_result(
        code=HttpCode.paramserror,
        message=message,
        data=None
    )


def server_error(message=""):
    return restful_result(
        code=HttpCode.servererror,
        message=message or "Internal Server Error",
        data=None
    )