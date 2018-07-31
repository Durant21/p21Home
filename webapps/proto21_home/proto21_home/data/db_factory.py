import os
import proto21_home
import sqlalchemy
import sqlalchemy.orm

from proto21_home.data.sqlalchemy_base import SqlAlchemyBase


class DbSessionFactory:
    __session_factory = None

    @classmethod
    def global_init(cls, db_filename):
        working_folder = os.path.dirname(proto21_home.__file__)
        file = os.path.join(working_folder, 'db', db_filename)
        conn_string = 'sqlite:///' + file

        # print("Connection string: " + conn_string)
        engine = sqlalchemy.create_engine(conn_string, echo=True)

        SqlAlchemyBase.metadata.create_all(engine)

        cls.__session_factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @classmethod
    def create_session(cls):
        return cls.__session_factory()