# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:09:41 2022

@author: Patricio Haro
"""

import math
n=int(input("n: "))
ex=1
suma=0
for i in range(n):
    v=pow(2,ex)
    ex=ex+1
    suma=suma+v
    v=suma
print(suma)