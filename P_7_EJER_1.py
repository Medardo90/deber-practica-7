# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:16:23 2022

@author: Patricio Haro
"""
import math
ba=int(input("base: "))
ex=int(input("exponente: "))
res=pow(ba, ex)
if ba < 0 or ex < 0:
    print("Error...!!!")
else:
   print(res)