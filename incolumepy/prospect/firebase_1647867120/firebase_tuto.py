# !/usr/bin/env python
# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials

sfb_count = 'firebase-adminsdk-c4mar@incolumepy-firebase-prospect.iam.gserviceaccount.com'

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

