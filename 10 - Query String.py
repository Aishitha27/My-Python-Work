# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:50:44 2023

@author: Cashapona
"""



import requests

url_get = 'http://httpbin.org/get'
payload = {"name": "Joseph", "ID": "123"}
r = requests.get(url_get, params=payload)
print(r.url)
print(r.status_code)
print(r.headers)