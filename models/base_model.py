#!/usr/bin/python3
""" class BaseModel that defines all common
    attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """ class BaseModel that defines all common
        attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
            of an instance. A key __class__ must be added to this dictionary
            with the class name of the object. created_at and updated_at must
            be converted to string object in ISO format
        """
        a_dict = {}
        a_dict = self.__dict__
        a_dict["__class__"] = self.__class__.__name__
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        return a_dict
