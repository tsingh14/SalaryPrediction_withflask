# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:43:42 2022

@author: singh
"""

import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':2.0,})
print(r.json())

url2 = 'http://localhost:5000/apilist'
r2 = requests.post(url2,json={'exp':[2.5,1.5,6.0]})
print(*r2.json(), sep ="\n")