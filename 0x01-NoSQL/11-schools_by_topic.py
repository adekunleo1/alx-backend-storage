#!/usr/bin/env python3
"""pymongo module to retrieve school list"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools
