#!/usr/bin/env python3
"""pymongo module to retrieve list"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """A function that returns the list of school having a specific topic"""
    query = {"topics": topic}
    schoolst = mongo_collection.find(query)
    return schools
