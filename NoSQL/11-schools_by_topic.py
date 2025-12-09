#!/usr/bin/env python3
""" 11-schools_by_topic.py """
def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic in their 'topics' field.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        list of matching school documents
    """
    if mongo_collection is None:
        return []

    # Rechercher les documents où 'topics' contient le topic
    return list(mongo_collection.find({"topics": topic}))
