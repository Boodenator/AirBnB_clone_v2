#!/usr/bin/python3
""" Review  class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Reviewclass"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
