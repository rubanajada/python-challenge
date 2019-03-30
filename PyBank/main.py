import os
import csv
budget_data = os.path.join("..","PyBank","budget_data.csv")
total_months = 0
total_profit_losses = 0
value = 0
change = 0
dates = []
profits_losses = []
with open(budget_data, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months =total_months+1
    total_profit_losses =total_profit_losses+ int(first_row[1])
    value = int(first_row[1])
    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profits_losses.append(change)
        value = int(row[1])
        
        total_months=total_months+ 1
        total_profit_losses = total_profit_losses + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits_losses)
    greatest_index = profits_losses.index(greatest_increase)
    greatest_date = dates[greatest_index]
    greatest_decrease = min(profits_losses)
    worst_index = profits_losses.index(greatest_decrease)
    worst_date = dates[worst_index]
    avg_change = sum(profits_losses)/len(profits_losses)
    

print("Financial Analysis")
print("---------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_losses)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("result.txt", "w")

line1 = "Financial Analysis"
line2 = "------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_losses)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))