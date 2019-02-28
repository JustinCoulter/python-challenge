#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 08:50:05 2019

@author: justincoulter
"""
#PyBank


import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

txt = open("PyBank_Output","w+")

print("Financial Analysis")
txt.write("Financial Analysis\r\n")
print("-------------------------------------------")
txt.write("------------------------------------------\r\n")



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
    
    #count the rows to determine month count
    #return the Total Profit by summing the 2nd index of all rows
    
    for row in csvreader:
       
       rowCount += 1           
       rowProfit = row[1]       
       totalProfit += int(rowProfit)
       profitList.append(int(rowProfit))
       month = row[0]
       monthList.append(month)
           
        
    print(f"Total Months: {rowCount}")
    txt.write(f"Total Months: {rowCount}\r\n")
    print(f"Total: ${totalProfit}")  
    txt.write(f"Total: ${totalProfit}\r\n") 
    #print(profitList)
    
    change = 0
    changeList =[]
    p = 0
    
    #create a list of the changes in profits/losses per month    
    for p in range(len(profitList) - 1):
        
            m = p + 1
            pI = int(profitList[p])
            pNxt = int(profitList[m])
            change = pNxt -pI
            changeList.append(change)
            
    avgChange = round((sum(changeList))/m,2)
   
    #determine the max change
    mx = max(changeList) 
    mxindex = changeList.index(mx)
    
    #determine the min change
    mn = min(changeList)  
    mnindex = changeList.index(mn)       
    monthList.pop(0)
    
    print(f"Average Change: ${avgChange}")
    txt.write(f"Average Change: ${avgChange}\r\n")
    print(f"Greatest Increase in Profits: {monthList[mxindex]} (${mx})")
    txt.write(f"Greatest Increase in Profits: {monthList[mxindex]} (${mx})\r\n")
    print(f"Greatest Decrease in Profits: {monthList[mnindex]} (${mn})")
    txt.write(f"Greatest Decrease in Profits: {monthList[mnindex]} (${mn})\r\n")
            
txt = open("PyBank_Output","w+")

