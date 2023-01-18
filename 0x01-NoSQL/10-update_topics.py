#!/usr/bin/env python3
"""pymongo module changes all topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """function updates all topics of a school documents"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    query = {"name": name}
    newValues = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, newValues)
