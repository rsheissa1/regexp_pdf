#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 22:37:42 2022

@author: rsheissa
"""

import re

with open("produccion_filtrados.txt", "r") as f:
    for line in f:
        print(line.split(','))