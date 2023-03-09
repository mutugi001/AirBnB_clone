#!/usr/bin/python3
import uuid
import datetime
"""class basemodel creation"""


class BaseModel:
    """initialization of class basemodel"""
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        print("{} {} {}".format(__class__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict keys = __dict__()
        keys.append(__class__)
        self.__dict__ = 
        

