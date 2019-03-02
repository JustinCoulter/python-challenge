#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:42:16 2019

@author: justincoulter
"""

#PyBoss


import os
import csv
import datetime

csvpath = os.path.join("employee_data.csv")
csvpath2 = os.path.join("employee_data2.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    # Read the header row first 
    csv_header = next(csvreader)
    
    employee = {}
    employee_list = []
 # create a list of dictionaries, one dictionary for each employee   
    for row in csvreader:
        employee = {"empID":row[0],"name":row[1],"dob":row[2],"ssn":row[3],"state":row[4]}
        employee_list.append(employee)

    #print(employee_list)

#open second data file
with open(csvpath2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    # Read the header row first 
    csv_header = next(csvreader)
    
    employee2 = {}
    #employee_list = []
    
#add second data file to employee list so all data is one list
    
    for row in csvreader:
        employee2 = {"empID":row[0],"name":row[1],"dob":row[2],"ssn":row[3],"state":row[4]}
        employee_list.append(employee2)

#print(employee_list)
#count = 0

#create a list for all the Employee ID numbers        
ID_list = []
for row in range(len(employee_list)):
    ID_list.append(employee_list[row]["empID"])
#print(ID_list)    
    
# ceate a list with employees name        
name_list = []
for row in range(len(employee_list)):
    name_list.append(employee_list[row]["name"])
    #count += 1
#print(name_list)
#print(count)
 
first_list = []  
last_list = []     
   
# split name list into first and last 
   
for n in range(len(name_list)):
    nme = name_list[n]          #create a list with (First and last name) as list items
    f,l = nme.split()           #seperate first and last name to their own lists
    first_list.append(f)
    last_list.append(l)
        
#print(first_list)
#print(last_list)

#create a list of birthdays   
DOB_list = []
for row in range(len(employee_list)):
    DOB_list.append(employee_list[row]["dob"])

#print(DOB_list)
    
#format birthdays and create a new list
dob_list = []
for i in DOB_list:
    dbl = [datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%m/%d/%Y')]
    dob_list.append(dbl)
#print(dob_list)

#create a new list of just ssn
ssn_list =[]
for row in range(len(employee_list)):
    ssn_list.append(employee_list[row]["ssn"])
#print(ssn_list)
#hide all but the last 4 digits of ssn, create a new list
hide_list =[]
for i in range(len(ssn_list)):
    ss = ssn_list[i]
    x,y,z = ss.split("-")
    last4 = z
    #print(z)
    hide_list.append("***-**-" + last4)
#print(hide_list)



 



