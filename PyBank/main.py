#PyBank

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:14:23 2019

@author: justincoulter
"""

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("___________________________________________")



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
   
    rowCount = 0
    totalProfit = 0
    avgChange = 0
    rowNext = 0
    profitList = []
    monthList = []
    
    #counts the rows to determine month count
    #returns the Total Profit by summing the 2nd index of all rows
    
    for row in csvreader:
       rowCount += 1           
       rowProfit = row[1]       
       totalProfit += int(rowProfit)
       profitList.append(int(rowProfit))
       month = row[0]
       monthList.append(month)
        
    print(f"Total Months: {rowCount}")
    print(f"Total: ${totalProfit}")   
    
    
    output = 0
    totalChange = 0.00
    totalChange = (sum(profitList) - profitList[0])/rowCount
    output = round(totalChange,2)
    
    print(f"Average Change: ${output}")

    pM = 0
    pL = 0
    diff = []
    for i in range(len(profitList)):
        pL = profitList[i]
        pM = profitList[i - 1]
        profitChange = (int(pL) - int(pM))
        diff.append(profitChange)
        
  
    mx = max(diff) 
    mxindex = diff.index(mx)
    
    mn = min(diff)  
    mnindex = diff.index(mn)       
    
    print(f"Greatest Increase in Profits: {monthList[mxindex]} (${mx})")
    print(f"Greatest Decrease in Profits: {monthList[mnindex]} (${mn})")
        
        