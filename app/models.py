from app import db


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

    def __init__(self, attr, branch, pname, enable, created_at, last_activity_at, date=None):
        self.project_id = attr.get('id')
        self.description = attr.get('description')
        self.project_name = attr.get('name')
        self.branch_name = branch.get('name')
        self.pname = pname
        self.enable = enable
        self.is_default_branch = branch.get('default')
        self.date = date or '2021-10-01'
        self.created_at = created_at
        self.last_activity_at = last_activity_at
