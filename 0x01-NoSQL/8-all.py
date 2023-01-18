#!/usr/bin/env python3
""" A Python module that lists all documents in a collection """


def list_all(mongo_collection):
    """
    Funtion lists all documents in a collection
    """
    docs = []

    if mongo_collection is None:
        return docs

    for c in mongo_collection.find({}):
        docs.append(c)

    return docs
