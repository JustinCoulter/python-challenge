
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:14:23 2019

@author: justincoulter
"""
#PyPoll


import os
import csv 
import pprint

csvpath = os.path.join("Resources", "election_data.csv")

#txt = open("PyPoll_Output","w+")

print("Election Results")
#txt.write("Election Results\r\n")
print("-" * 40)
#txt.write("--------------------------------------\r\n")





with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    
    rowCount = 0
    
    for row in csvreader:
        
        rowCount += 1
        
        
    print(f"Total Votes: {rowCount}")
#    txt.write(f"Total Votes: {rowCount}\r\n")
    print("-" * 40)
#    txt.write("--------------------------------------\r\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    