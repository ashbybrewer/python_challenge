import csv

# open and read the CSV file
with open("Resources/budget_data.csv", "r") as file:
    reader = csv.reader(file)
    
    # storing the header row
    header = next(reader)
    data = list(reader)

#calculating total months and total profit/loss  

total_months = len(data)
total_amount = sum(int(row[1]) for row in data)

# calculating changes and then the average
changes = [int(data[i+1][1]) - int(data[i][1]) for i in range(total_months - 1)]
avg_change = sum(changes) / len(changes)

#identifying greatest increase and decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = data[changes.index(greatest_increase) + 1][0]
greatest_decrease_date = data[changes.index(greatest_decrease) + 1][0]


#formatting the results 
result= (
    "Financial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

#print results 
print(result)

#save results to txt file
with open("analysis/financial_analysis.txt", "w") as file:
    file.write(result)
