#Importing the necessary modules/libraries
import os
import csv

# Set filepath
data_file = "budget_data.csv"

# Create lists
total_months = []
total_profit = []
monthly_profit_changes = []

with open(data_file) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    for row in csvreader:
        print(row) 
      
    # Append the total months and total profit
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Monthly changes in profits
    for i in range(len(total_profit)-1):

        monthly_profit_changes.append(total_profit[i+1]-total_profit[i])