#!/usr/bin/env python3
""" 9-insert_school.py """
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection using keyword arguments
    Args:
        mongo_collection: pymongo collection object
        **kwargs: key/value pairs representing document fields
    Returns:
        _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
