#!/usr/bin/env python3
""" 10-update_topics.py """
def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all school documents with the given name.
    
    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list of str): list of topics to set
    """
    mongo_collection.update_many(
        {"name": name},           # filtre : tous les documents avec ce nom
        {"$set": {"topics": topics}}  # mise à jour : remplace le champ 'topics'
    )
