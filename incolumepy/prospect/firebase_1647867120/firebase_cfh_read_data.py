"""Firebase read data examples."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

from pathlib import Path
from pprint import pprint

import firebase_admin
from firebase_admin import credentials, firestore

service_account_key = (
    Path("~")
    .expanduser()
    .joinpath(
        "projetos",
        "authkeys",
        "incolumepy-firebase-prospect-firebase-adminsdk-c4mar-ea5393e416.json",
    )
)

cred = credentials.Certificate(service_account_key)
firebase_admin.initialize_app(cred)

db = firestore.client()


def read_data_by_id():
    """Read data by id."""
    keys = [
        "zvO9zuUTBirf8PwRs1i0",  # auto id
        "janedoe",  # known id
    ]
    for key in keys:
        result = db.collection("people").document(key).get()
        print(type(result), key, result.to_dict())


def read_all_collection():
    """Read all collection."""
    docs = db.collection("people").get()
    for doc in docs:
        print(doc.to_dict())


def quering_collection():
    """Query collections."""
    docs = db.collection("person").where("age", "<", 40).get()
    for doc in docs:
        print("<40", doc.to_dict())
    docs = db.collection("person").where("age", ">", 40).get()
    for doc in docs:
        print(">40", doc.to_dict())


def quering_collection_container():
    """Query collection container."""
    docs = (
        db.collection("person")
        .where("socials", "array_contains", "youtube")
        .get()
    )
    print("youtube")
    pprint([doc.to_dict() for doc in docs])

    docs = (
        db.collection("person")
        .where("socials", "array_contains", "instagram")
        .get()
    )
    print("instagram")
    pprint([doc.to_dict() for doc in docs])

    docs = (
        db.collection("person")
        .where("address", "in", ["Brazil", "India", "Turkey", "USA"])
        .get()
    )
    print("address")
    pprint([doc.to_dict() for doc in docs])


def run():
    """Run it."""
    read_data_by_id()
    read_all_collection()
    quering_collection()
    quering_collection_container()


if __name__ == "__main__":  # pragma: no cover
    run()
