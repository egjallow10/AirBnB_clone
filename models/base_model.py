#!/usr/bin/python3
"""The Base ClassI"""

import datetime
import uuid
import models



class BaseModel:
    """Defining a base class model

    This model perform serialization/deserialization
    """

    def _init__(self, *args, **kwargs):
        """base model attributes

        arg:
            self.id: uuid.uuid4()
            generate unique id for every basemodel attribute
            self.created_at create date and time when instance created
            self.updated_at create date and time when instance is created
            and update every time object is changed
        """

        if kwargs:
            for kwargs, val in kwargs.item():
                if kwargs in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                elif kwargs == '__class__':
                    continue
                setattr(self, kwargs, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}], ({}), {}".formart(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """updates the public instance attribute
        with the current datetime
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """diplaying class information"""
        class_info = self.__dict__.copy()
        class_info['__class__'] = self.__class__.__name__
        class_info['created_at'] = self.created_at.isoformat()
        class_info['updated_at'] = self.updated_at.isoformat()

        return class_info
