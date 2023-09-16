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


import time
from datetime import datetime, timedelta

import pytz

tz = pytz.timezone('Asia/Shanghai')  # 东八区

month_abbr = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
              'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}


def get_short_time(timestamp: float) -> str:
    t = datetime.fromtimestamp(timestamp / 1000, pytz.timezone('Asia/Shanghai')).strftime('%H:%M:%S')

    return t


def get_full_time(timestamp: float) -> str:
    t = datetime.fromtimestamp(timestamp / 1000, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

    return t


def get_now_date():
    t = datetime.fromtimestamp(time.time(), pytz.timezone('Asia/Shanghai')).strftime(
        '%Y-%m-%d')
    return t


def get_now_time():
    t = datetime.fromtimestamp(time.time(), pytz.timezone('Asia/Shanghai')).strftime(
        '%Y-%m-%d %H:%M:%S')
    return t


def str2time(raw_time_str: str):
    if ('T' in raw_time_str) and ('Z' in raw_time_str):  # 2016-01-01T00:00:00Z
        new_str = raw_time_str.replace('T', ' ').replace('Z', '').split('.')[0]
    else:
        new_str = raw_time_str
    return new_str


def timestamp_datetime(timestamp):
    if len(str(timestamp)):
        timestamp = timestamp / 1000
    return datetime.fromtimestamp(timestamp).date()


def timestamp_datetime_str(timestamp):
    date = timestamp_datetime(timestamp)
    return date.strftime('%Y-%m-%d %H:%M:%S')
