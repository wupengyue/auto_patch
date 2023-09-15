import logging

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from app.common import success_rsp, row2dict
from app.database import db
from app.services import project_case_list

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
def get_jira_bug_list():
    data = project_case_list(request.args)
    if data is None:
        return success_rsp(data=list(), total=0)
    return success_rsp(data=[row2dict(x) for x in data.items], total=data.total)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
