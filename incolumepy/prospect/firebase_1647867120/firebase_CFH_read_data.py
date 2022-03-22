# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import datetime

import firebase_admin
from firebase_admin import credentials
from pathlib import Path
from firebase_admin import firestore
from pprint import pprint


service_account_key = Path('~').expanduser().joinpath(
    'projetos', 'authkeys', 'incolumepy-firebase-prospect-firebase-adminsdk-c4mar-ea5393e416.json')

cred = credentials.Certificate(service_account_key)
firebase_admin.initialize_app(cred)

db = firestore.client()


def read_data_by_id():
    keys = [
        'zvO9zuUTBirf8PwRs1i0',  # auto id
        'janedoe',  # known id
    ]
    for key in keys:
        result = db.collection('people').document(key).get()
        print(type(result), key, result.to_dict())


def read_all_collection():
    docs = db.collection('people').get()
    for doc in docs:
        print(doc.to_dict())


def quering_collection():
    docs = db.collection('person').where('age', '<', 40).get()
    for doc in docs:
        print('<40', doc.to_dict())
    docs = db.collection('person').where('age', '>', 40).get()
    for doc in docs:
        print('>40', doc.to_dict())


def quering_collection_container():
    docs = db.collection('person').where('socials', 'array_contains', 'youtube').get()
    print('youtube')
    pprint([doc.to_dict() for doc in docs])

    docs = db.collection('person').where('socials', 'array_contains', 'instagram').get()
    print('instagram')
    pprint([doc.to_dict() for doc in docs])

    docs = db.collection('person').where('address', 'in', ['Brazil', 'India', 'Turkey', 'USA']).get()
    print('address')
    pprint([doc.to_dict() for doc in docs])


def run():
    # read_data_by_id()
    # read_all_collection()
    # quering_collection()
    quering_collection_container()
    pass


if __name__ == '__main__':  # pragma: no cover
    run()
