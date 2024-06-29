#!/usr/bin/python3

"""
Definition of errors produced in File Storage
"""


class ModelNotFoundError(Exception):
    """display error when unknown module is used"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class InstanceNotFoundError(Exception):
    """display error when unknown id  is used"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Instance of {mod} with id {obj_id} does not exist!")
