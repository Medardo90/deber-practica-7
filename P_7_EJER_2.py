# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:32:34 2022

@author: Patricio Haro
"""
import math
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a == 0:
    print("División para cero")
else:
    negb=b*-1
    b2=pow(b, 2)
    re1=4*a*c
    re2=b2-re1
    if re2<0:
        print("Raíz negativa")
    else:
        re3=math.sqrt(re2)
        re4=2*a
        xp=(negb+re3)/(re4)
        xn=(negb-re3)/(re4)
        if xp==xn:
            print("Única solución:")
            print("x=",xp)
        if xp!=xn:
            print("Dos soluciones:")
            print("x1=",xp)
            print("x2=",xn)
            
