# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:01:07 2020

@author: wyue
"""

import csv

counts = {}
with open('Data/ReadCSV.csv','r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        
        lastname = row['Last_Name']
        if lastname in counts:
            counts[lastname] +=1
        else:
            counts[lastname] = 1

for ln, count in counts.items():
    print(ln,count, sep=':')
