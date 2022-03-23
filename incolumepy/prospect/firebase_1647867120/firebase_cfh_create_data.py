"""Firebase add data examples."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import datetime
from pathlib import Path

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


def add_record():
    """Add collection and document."""
    data = {
        "name": "Ricardo",
        "age": 44,
        "address": "Brasil",
        "socials": [
            "linkedin",
            "facebook",
            "telegram",
            "instagram",
            "twiter",
            "github",
            "gitlab",
        ],
    }
    db.collection("my-collection").add(data)
    db.collection("my-collection/decretos/2022").add(data)
    db.collection("my-collection/decretos/2022").document("A0001").set(data)
    db.collection("my-collection").document("D0001").set(data)
    db.collection("my-collection").document("D0002").set(
        {"name": "Brito", "age": 2, "socials": ["github"]}
    )
    db.collection("person").document("D0001").set(data)


def add_data_auto_id0():
    """Add data auto id."""
    db.collection("person").add(
        {"name": "John Walking", "age": 54, "employed": True, "address": None}
    )


def add_data_auto_id():
    """Add data auto id."""
    data = {"name": "Jane Doe", "age": 14, "employed": False, "address": "USA"}
    db.collection("person").add(data)


def add_data_auto_way2_id():
    """Add data auto id other way."""
    data = {
        "name": "Jane Doe",
        "age": 24,
        "employed": False,
        "address": "Canada",
    }
    db.collection("people").document().set(data)


def add_data_known_id():
    """Add data known id."""
    data = {
        "name": "Jane Doe",
        "age": 34,
        "employed": False,
        "address": "Turkey",
    }
    db.collection("people").document("janedoe").set(data)


def add_atos_structure():
    """Atos structure."""
    tipos = [
        "alvara",
        "carta",
        "decreto",
        "decreto-lei",
        "lei",
        "medida-provisoria",
    ]
    years = [1808, 1978, 1996, 2006, 2009, 2011, 2022]
    data = {
        "epigrafe": "Ato Fake",
        "date": datetime.datetime.now().strftime("%F"),
    }
    db.collection("atos/fake/2022").document("A00001").set(data)
    db.collection("atos").document("fake").collection("2022").add(
        {"epigrafe": "ato fake nº 2"}
    )
    db.collection("atos").document("fake").collection("2022").document().set(
        {"epigrafe": "ato fake nº 4"}
    )
    db.collection("atos").document("fake").collection("2022").document(
        "A00005"
    ).set({"epigrafe": "ato fake nº 5"})
    for tipo in tipos:
        for year in years:
            db.collection(f"ato/{tipo}/{year}").document().set(data)


def update_data_by_id():
    """Update data by id."""
    data = {"employed": True, "address": "London"}
    db.collection("people").document("janedoe").set(data, merge=True)


def sub_collection_add():
    """Add subcollection."""
    db.collection("people").document("janedoe").collection("movies").add(
        {"title": "Avengers"}
    )


def run():
    """Run it."""
    add_record()
    add_data_auto_id()
    add_data_auto_way2_id()
    add_data_known_id()
    add_atos_structure()
    update_data_by_id()
    sub_collection_add()


if __name__ == "__main__":  # pragma: no cover
    run()
