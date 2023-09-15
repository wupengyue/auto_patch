from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, pool_recycle=3600, pool_pre_ping=True,
                       isolation_level="READ UNCOMMITTED", pool_size=200)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def session_commit(db):
    """Provide a transactional scope around a series of operations."""
    session = db.session
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import models.model
    Base.metadata.create_all(bind=engine)
