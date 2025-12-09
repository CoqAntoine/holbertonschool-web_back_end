#!/usr/bin/env python3
""" 8-all.py """
def list_all(mongo_collection):
    """
    Returns all documents in a collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        list of documents, or empty list if none
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
