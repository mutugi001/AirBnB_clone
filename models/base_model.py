#!/usr/bin/python3
import uuid
import datetime
"""class basemodel creation"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())
        self.updated_at = str(datetime.datetime.now)

    def __str__(self):
        print("{} {} {}".format(__class__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now.isoformat()

    def to_dict(self):

        keys_dict = self.__dict__.copy
        keys_dict['__class__'] = type(self).__name__
        keys_dict['created_at'] = self.created_at.isoformat()
        keys_dict['updated_at'] = self.updated_at.isoformat()
        return keys_dict
