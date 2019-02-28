#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:01:32 2019

@author: justincoulter
"""

#PyPoll


import os
import csv 


csvpath = os.path.join("Resources", "election_data.csv")

txt = open("PyPoll_Output","w+")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    
    rowCount = 0
    
    voter_list = []
    
    for row in csvreader:
        
        rowCount += 1 
        #create a dictionary for each vote
        voter = {"voterID":row[0],"county":row[1],"candidate":row[2]}
        #add the dictionaries into a list
        voter_list.append(voter)                
    
    
    candidates_list = []     #list of all candidates read from dictionary including duplicates
    
    for vote in range(len(voter_list)):
        
        candidates_list.append(voter_list[vote]["candidate"]) 
    
        
    candidate_list = []      #list of each candidate
    for i in candidates_list:       #removes duplicates in candidates_list
        if i not in candidate_list: 
            candidate_list.append(i)   
            
            
    vote_count_list = []            #make a list of vote count per candidate
    
    for i in range(len(candidate_list)):
        vote_count = 0
        for x in range(len(candidates_list)):
            
            if candidates_list[x] == candidate_list[i]:
                vote_count += 1
        vote_count_list.append(vote_count)
   
    total_votes = sum(vote_count_list)      #calculate total vote count
    
    # print header for results
    print("Election Results")
    txt.write("Election Results\r\n")
    print("-" * 40)
    txt.write("----------------------------------------------------------\r\n")

    #print total votes
    print(f"Total Votes: {total_votes}")
    txt.write(f"Total Votes: {total_votes}\r\n")    
    print("-" * 40)
    txt.write("----------------------------------------------------------\r\n")
    
    #calculate and print vote percent and total vote count per candidate
    for a in range(len(candidate_list)):
        vote_percent = 0
        vote_percent = round(((vote_count_list[a] / total_votes)*100),3)
        print(f"{candidate_list[a]}: {vote_percent}% ({vote_count_list[a]})")
        txt.write(f"{candidate_list[a]}: {vote_percent}% ({vote_count_list[a]})\r\n")
    
    print("-" * 40)
    txt.write("----------------------------------------------------------\r\n")
    
    #determine and print candidate with the maximum votes and respective count
    print(f"Winner: {candidate_list[vote_count_list.index(max(vote_count_list))]}")
    txt.write(f"Winner: {candidate_list[vote_count_list.index(max(vote_count_list))]}\r\n")
    
    print("-" * 40)
    txt.write("----------------------------------------------------------\r\n")    
    
txt = open("PyPoll_Output","w+")       
            
