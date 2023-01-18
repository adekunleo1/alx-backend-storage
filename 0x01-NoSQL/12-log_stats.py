#!/usr/bin/env python3
"""A Python script providing stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(nginx.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(nginx.count_documents(
        {"method": "POST"})))
    print("\tmethod PUT: {}".format(nginx.count_documents(
        {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(nginx.count_documents(
        {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(nginx.count_documents(
        {"method": "DELETE"})))
    print("{} status check".format(nginx.count_documents(
        {"method": "GET"} and {"path": "/status"})))
    client.close()
