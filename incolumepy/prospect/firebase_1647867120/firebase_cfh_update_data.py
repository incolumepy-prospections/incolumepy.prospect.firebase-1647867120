"""Firebase update data examples."""
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


def update_data_wrong_value_known_id():
    """Valor errado."""
    db.collection("person").document("d1").update({"age": 30})


def update_data_ubsent_value_known_id():
    """Campo faltando."""
    db.collection("person").document("d1").update(
        {"birthdate": datetime.datetime(1992, 1, 1, 12, 0)}
    )


def update_data_multiples_values_known_id():
    """Multiplos valores."""
    db.collection("person").document("d1").update(
        {"age": 50, "birthdate": datetime.datetime(1972, 1, 1)}
    )


def update_data_increment_value_known_id():
    """Incremento de valores."""
    db.collection("person").document("d1").update(
        {"age": firestore.Increment(10)}
    )


def update_data_containers_known_id():
    """Remove socials: whatsup."""
    db.collection("person").document("d1").update(
        {"socials": firestore.ArrayRemove(["whatsup"])}
    )
    # union socials: linkedin
    db.collection("person").document("d1").update(
        {"socials": firestore.ArrayUnion(["linkedin"])}
    )


def update_data_unknown_id():
    """Update data unknown id."""
    docs = db.collection("person").get()
    for doc in docs:
        # print(doc.to_dict())
        if 40 <= doc.to_dict()["age"] < 50:
            key = doc.id
            db.collection("person").document(key).update(
                {"agegroup": "middle age"}
            )
        elif 50 <= doc.to_dict()["age"] < 60:
            db.collection("person").document(doc.id).update(
                {"agegroup": "middle top age"}
            )
        else:
            db.collection("person").document(doc.id).update(
                {"agegroup": "better age"}
            )


def update_data_by_query_unknown_id():
    """Update data by query unknown id."""
    docs = (
        db.collection("person")
        .where("age", "<", 40)
        .where("age", ">=", 30)
        .get()
    )
    for doc in docs:
        # print(doc)
        db.collection("person").document(doc.id).update(
            {"agegroup": "middle bottom age"}
        )

    docs = db.collection("person").where("age", "<", 30).get()
    _ = [
        db.collection("person")
        .document(doc.id)
        .update({"agegroup": "juvenil"})
        for doc in docs
    ]
    docs = db.collection("person").where("age", "<", 18).get()
    _ = [
        db.collection("person")
        .document(doc.id)
        .update({"agegroup": "adolescente"})
        for doc in docs
    ]
    docs = db.collection("person").where("age", "<", 12).get()
    _ = [
        db.collection("person").document(doc.id).update({"agegroup": "kid"})
        for doc in docs
    ]
    docs = db.collection("person").where("age", "<", 3).get()
    _ = [
        db.collection("person").document(doc.id).update({"agegroup": "baby"})
        for doc in docs
    ]


# def update
def run():
    """Run it."""
    update_data_containers_known_id()
    update_data_unknown_id()
    update_data_by_query_unknown_id()


if __name__ == "__main__":  # pragma: no cover
    run()
