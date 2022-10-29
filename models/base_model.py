#!/usr/bin/python3
"""The Base ClassI"""

from datetime import datetime
import uuid
import models



class BaseModel:
    """Defining a base class model

    This model perform serialization/deserialization
    """

    def __init__(self, *args, **kwargs):
        """base model attributes

        arg:
            self.id: uuid.uuid4()
            generate unique id for every basemodel attribute
            self.created_at create date and time when instance created
            self.updated_at create date and time when instance is created
            and update every time object is changed
        """

        if kwargs:
            for k, val in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                elif kwargs == '__class__':
                    continue
                setattr(self, k, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """if new intance has made we calling a new method"""
            models.storage.new(self)

    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>")"""
        return "[{}], ({}), {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """updates the public instance attribute
        with the current datetime
        """
        self.updated_at = datetime.now()
        """save the new(self) method"""
        models.storage.save()
        return


    def to_dict(self):
        """diplaying class information"""
        dict_info = self.__dict__.copy()
        dict_info['__class__'] = self.__class__.__name__
        dict_info['created_at'] = self.created_at.isoformat()
        dict_info['updated_at'] = self.updated_at.isoformat()
        return dict_info
