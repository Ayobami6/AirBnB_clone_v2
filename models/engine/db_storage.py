#!/usr/bin/python3
"""Database connection module."""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


USER = getenv("HBNB_MYSQL_USER")
PWD = getenv("HBNB_MYSQL_PWD")
HOST = getenv("HBNB_MYSQL_HOST")
DB = getenv("HBNB_MYSQL_DB")
ENV = getenv("HBNB_ENV")


class DBStorage:
    """Database storage class for dbstorage instance creation."""

    __engine = None
    __session = None

    classes = {
        'State': State,
        'City': City,
        'Place': Place,
        'Review': Review,
        'User': User,
        'Amenity': Amenity
    }

    def __init__(self):
        """Dbstorage constructor."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)
        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Get all item from db if cls is none or get all from the specified cls.

        ...
        """
        data_dict = {}
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                data_dict[key] = obj

        else:
            for item_cls in self.classes.values():
                for obj in self.__session.query(item_cls).all():
                    key = "{}.{}".format(item_cls.__name__, obj.id)
                    data_dict[key] = obj
        return data_dict

    def new(self, obj):
        """Add new object to database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to database."""
        self.__session.commit()

    def delete(self, obj):
        """Delete the object from the database."""
        if obj is None:
            pass
        else:
            [cname, o_id] = obj.split(".")
            cls = self.classes[cname]
            t_obj = self.__session.query(cls).filter(
                cls.id == o_id).one_or_none()
            if t_obj is not None:
                self.__session.delete(t_obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()

    def close(self):
        """ Close storage session
        """
        self.__session.close()
