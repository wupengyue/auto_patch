from app.models import ProjectCase
from sqlalchemy import and_, desc


def project_case_list(args):
    page = int(args.get('page')) if args.get('page') else 1
    limit = int(args.get('limit')) if args.get('limit') else 10
    # http://localhost:9528/projectcase/list?page=1&limit=20&case_id=3&case_type=2
    case_type = args.get('case_type')
    case_id = args.get('case_id')
    data = None
    if (case_type is None) and (case_id is None):
        data = ProjectCase.query.order_by(desc(ProjectCase.case_id)).paginate(page=page, per_page=limit,
                                                                              error_out=False, count=True)
    if case_type and case_id:
        ProjectCase.query.filter(and_(ProjectCase.case_type == case_type, ProjectCase.case_id == case_id)).order_by(
            desc(ProjectCase.case_id)).paginate(page=page, per_page=limit, error_out=False, count=True)
    if case_type and (case_id is None):
        data = ProjectCase.query.filter(ProjectCase.case_type == case_type).order_by(
            desc(ProjectCase.case_id)).paginate(page=page, per_page=limit, error_out=False, count=True)
    if case_id and (case_type is None):
        data = ProjectCase.query.filter(ProjectCase.case_id == case_id).order_by(desc(ProjectCase.case_id)).paginate(
            page=page, per_page=limit, error_out=False, count=True)

    return data
