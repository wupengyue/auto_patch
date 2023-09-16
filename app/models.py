from app import db
from app.common import get_now_time


# generate code
# pip install  flask-sqlacodegen
# flask-sqlacodegen mysql://wpy:WpY%401234@10.86.30.7/jira?charset=utf8mb4  --outfile "models.py" --flask


class ProjectCase(db.Model):
    __tablename__ = 'project_case'

    case_id = db.Column(db.Integer, primary_key=True)
    case_serial_number = db.Column(db.Integer)
    case_sign = db.Column(db.String(500))
    case_name = db.Column(db.String(200))
    project_id = db.Column(db.Integer)
    module_id = db.Column(db.Integer)
    case_type = db.Column(db.Integer)
    failcontinue = db.Column(db.Integer)
    create_by = db.Column(db.String(64))
    create_time = db.Column(db.Date)
    update_by = db.Column(db.String(64))
    update_time = db.Column(db.Date)
    remark = db.Column(db.String(200))

    def __init__(self, content):
        self.case_id = content.get('case_id')
        self.case_serial_number = content.get('case_serial_number')
        self.case_sign = content.get('case_sign')
        self.case_name = content.get('case_name')
        self.project_id = content.get('project_id')
        self.module_id = content.get('module_id')
        self.case_type = content.get('case_type')
        self.failcontinue = content.get('failcontinue')
        self.create_by = content.get('create_by')
        self.create_time = get_now_time()
        self.update_by = content.get('update_by')
        self.update_time = get_now_time()
        self.remark = content.get('remark')
