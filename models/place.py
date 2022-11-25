#!/usr/bin/python3
"""
This is 'place' module.
Functions and Classes:
    class Place(BaseModel):
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """representing a place"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
