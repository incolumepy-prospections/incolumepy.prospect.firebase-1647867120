# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import firebase_admin
from firebase_admin import credentials
from pathlib import Path
from firebase_admin import firestore


service_account_key = Path('~').expanduser().joinpath(
    'projetos', 'authkeys', 'incolumepy-firebase-prospect-firebase-adminsdk-c4mar-ea5393e416.json')

cred = credentials.Certificate(service_account_key)
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('person').add({'name': 'Ricardo', 'age': 44})
