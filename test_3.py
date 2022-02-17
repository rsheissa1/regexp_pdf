#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:59:40 2022

@author: rsheissa
"""


with open("generales_filtrados.txt", "r") as f:
    for line in f:
        lineaLimpia1 = line.strip('\n')
        lineaLista1 = lineaLimpia1.split(",")
        print(f"{lineaLista1} \n")



f.close()