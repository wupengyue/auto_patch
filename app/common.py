from flask import make_response, jsonify


class ResCode(object):
    ok = 20000
    un_auth_error = 401
    params_error = 400
    server_error = 500


def success_rsp(message="", data=None, total=None):
    return restful_result(code=ResCode.ok, message=message, data=data, total=total)


def error_rsp(message="", data=None, code=ResCode.server_error, status_code=500):
    return restful_result(code=code, message=message, data=data, status_code=status_code)


def restful_result(code, message, data, total=None, status_code=200):
    """
    :param code: 业务code
    :param message:
    :param data:
    :param total:
    :param status_code: http status code
    :return:
    """
    if not data:
        if isinstance(data, list):
            pass
        else:
            data = {}

    res = {"code": code, "message": message, "data": data, "total": None}
    if total:
        res['total'] = total
    return make_response(jsonify(res), status_code)


def row2dict(row, skip=None):
    d = {}
    for column in row.__table__.columns:
        if skip and column.name in skip:
            continue
        value = getattr(row, column.name)
        d[column.name] = str(value) if value else ''

    return d
