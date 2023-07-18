#!/usr/bin/env python3
'''a Python function that inserts a new document in a collection based on kwargs'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''insert_one and return the id'''
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
