# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
from pprint import pprint

__author__ = "@britodfbr"  # pragma: no cover

url = 'https://incolumepy-firebase-prospect-default-rtdb.asia-southeast1.firebasedatabase.app/atos{}'

ato_fake = {
    'epigrafe': '', 'content': 'texto ato',
    'num': 0, 'classify': 'dec',
}


def add_data(num):
    """Adicionar dados com post."""
    ato_fake.update({'num': num, 'classify': 'dec'})
    req = requests.post(url.format(f'/decreto/.json'), data=json.dumps(ato_fake))
    print(req, req.text)


def add_key_data(num, tipo=None, classify=None, dou=None, date=None):
    """Adicionar dados com put."""
    tipo = tipo or 'decreto'
    classify = classify or 'dec'
    dou = dou or 'DOU p.02 http://in.gov.br'
    date = date or datetime.now().strftime('%F %T')
    ato_fake.update(
        {
            'dou': dou,
            'date': date,
            'num': num,
            'epigrafe': f'{tipo} nº {num} de {datetime.now().strftime("%d de %B de %Y")}',
            'classify': classify
        }
    )
    req = requests.put(url.format(f'/{tipo}/{tipo[0].upper()}{num:0>4}.json'), data=json.dumps(ato_fake))
    print(req, req.text)


def change_data():
    ato_fake.update({'classify': 'DIM'})
    req = requests.patch(url.format('/decreto/-MyhqoBUmGmmyjXaB3d6.json'), data=json.dumps(ato_fake))
    print(req, req.text)


def get_data():
    req = requests.get(url.format('.json'))
    print(req)
    print(req.content)
    pprint(req.json())


def get_lei_data():
    req = requests.get(url.format('/lei.json'))
    pprint(req.json())


def delete_lei():
    req = requests.delete(url.format('/lei/L0010.json'))
    print(req, req.text)


def delete_dec():
    req = requests.get(url.format('/decreto.json'))
    atos = req.json()
    for ato in atos:
        # print(ato)
        # print(atos[ato])
        if atos[ato]['classify'] == 'dec':
            r = requests.delete(url.format(f'/decreto/{ato}.json'))
            print(r, r.text)


def delete_dec_melhorado():
    req = requests.get(url.format('/decreto.json'))
    for key, ato in req.json().items():
        print(key, ato)
        if ato['num'] == 0:
            r = requests.delete(url.format(f'decreto/{key}.json'))
            print(r, r.text)


def run():
    for n in range(11):
        pass
        add_data(n)
        add_key_data(n, tipo='decreto', classify='DCM')
        add_key_data(n, tipo='lei', classify='LIM')
    change_data()
    get_data()
    get_lei_data()
    delete_lei()
    delete_dec()
    delete_dec_melhorado()


if __name__ == '__main__':  # pragma: no cover
    run()
