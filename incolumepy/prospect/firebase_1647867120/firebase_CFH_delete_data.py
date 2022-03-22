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


def delete_data_full():
    db.collection('my-collection').document('D0002').delete()


def delete_data_field():
    db.collection('my-collection').document('D0001').update({'socials': firestore.DELETE_FIELD})


def delete_data_unknown_id():
    """
    Remove elements no address.

    :return: None
    """
    docs = db.collection('my-collection').get()
    print(len(docs))
    for doc in docs:
        elem = doc.to_dict()
        key = doc.id
        print(key)
        if not elem.get('address'):    # no address
            print(elem)
            db.collection('my-collection').document(key).delete()


def run():
    delete_data_full()
    delete_data_field()
    delete_data_unknown_id()


if __name__ == '__main__':  # pragma: no cover
    run()
