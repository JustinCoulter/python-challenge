#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:42:16 2019

@author: justincoulter
"""

#PyBoss


import os
import csv

csvpath = os.path.join("employee_data.csv")
csvpath2 = os.path.join("employee_data2.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    # Read the header row first 
    csv_header = next(csvreader)
    
    employee = {}
    employee_list = []
    
    for row in csvreader:
        employee = {"empID":row[0],"name":row[1],"dob":row[2],"ssn":row[3],"state":row[4]}
        employee_list.append(employee)

    #print(employee_list)

with open(csvpath2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    # Read the header row first 
    csv_header = next(csvreader)
    
    employee2 = {}
    #employee_list = []
    
    for row in csvreader:
        employee2 = {"empID":row[0],"name":row[1],"dob":row[2],"ssn":row[3],"state":row[4]}
        employee_list.append(employee2)

#print(employee_list)
#count = 0
name_list = []
for row in range(len(employee_list)):
    name_list.append(employee_list[row]["name"])
    #count += 1
#print(name_list)
#print(count)
 
first_list = []  
last_list = []        # split name list into first and last 
   
for n in range(len(name_list)):
    nme = name_list[n]          #create a list with (First and last name) as list items
    f,l = nme.split()           #seperate first and last name to their own lists
    first_list.append(f)
    last_list.append(l)
        
#print(first_list)
nu_name_list = []
nu_name = {}
r =0
for r in range(len(employee_list)):
    nu_name = {"empID":r[0],"dob":r[2],"ssn":r[3],"state":r[4]}
    nu_name_list.append((nu_name[r]["empID"]["dob"]["ssn"]["state"]))
    
print(nu_name_list)
    
'''for n in range(len(nu_name_list)):
    
    for f in range(len(first_list)):
        nu_name = {"empID":n[0],"first_name":f[0],"dob":n[2],"ssn":n[3],"state":n[4]}
        nu_name_list.append(nu_name)'''
        
'''for l in range(len(last_list)):
    nu_name = {"empID":row[0],"first_name":f[0],"last_name":l[0],"dob":row[2],"ssn":row[3],"state":row[4]}
    nu_name_list.append(nu_name)'''










