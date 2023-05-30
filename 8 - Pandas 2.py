# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:42:30 2023

@author: Cashapona
"""

import requests
url = "https://www.ibm.com/"
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.request.body)







