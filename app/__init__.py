import logging

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from app.common import success_rsp, row2dict, error_rsp
from app.database import db
from app.services import project_case_list, create_project_case, update_project_case

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)


@app.route('/')
def index():
    return success_rsp("Auto Patch Services")


@app.route('/projectcase/list', methods=['GET'])
def fetch_project_case_list():
    data = project_case_list(request.args)
    if data is None:
        return success_rsp(data=list(), total=0)
    return success_rsp(data=[row2dict(x) for x in data.items], total=data.total)


@app.route('/projectcase/create', methods=['POST'])
def add_project_case():
    content = request.json
    res, msg = create_project_case(content)
    if res:
        return success_rsp(message=msg)
    else:
        return error_rsp(message=msg)


@app.route('/projectcase/update', methods=['POST'])
def updated_project_case():
    content = request.json
    res, msg = update_project_case(content)
    if res:
        return success_rsp(message=msg)
    else:
        return error_rsp(message=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
