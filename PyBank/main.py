import os
import csv

budget_csv = os.path.join(".","budget_data.csv")

# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    total_number_of_months = 0
    net_total = 0
    change = 0
    previous_value = 0
    monthly_change =[]
    greatest_increase = 0
    greatest_decrease = change

    # Index tracking for csv file for each line
    i = 1

    # Read through each row of data after the header
    for row in csvreader:
        total_number_of_months += 1
        net_total = net_total + int(row[1])
        
        if i == 1:
            change = 0
        else:
            change = int(row[1]) - previous_value
            monthly_change.append(change)
            if change > greatest_increase:
                greatest_increase = change
                month_greatest_increase = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                month_greatest_decrease = row[0]
        previous_value = int(row[1])
        i += 1
    
    # Calculating the Average Monthly Change
    total_change = 0
    for delta in monthly_change:
        total_change += delta

    
    mean_change = total_change/len(monthly_change)

    
    # Statistical Analysis Display
    #print (len(monthly_change))
    print ("Financial Analysis")
    print ("----------------------------")
    print ("Total Months:", total_number_of_months)
    print ("Total: $", net_total)
    print ("Average  Change: $", mean_change)
    #print ("Greatest Increase in Profits: " , max(monthly_change) )
    #print ("Greatest Decrease in Profits: ", min(monthly_change) )
    print ("Greatest Increase in Profits: " , month_greatest_increase, "$(", greatest_increase, ")")
    print ("Greatest Decrease in Profits: ", month_greatest_decrease, "$(" , greatest_decrease,")" )

# Write to an Output file
output_path = os.path.join(".", "Py_Bank_Output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

# Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')

    # Write to text file
    csvwriter.writerow (['Financial Analysis'])
    csvwriter.writerow (['----------------------------'])
    csvwriter.writerow (['Total Months:', total_number_of_months])
    csvwriter.writerow (['Total: $', net_total])
    csvwriter.writerow (['Average  Change: $', mean_change])
    csvwriter.writerow (['Greatest Increase in Profits:', month_greatest_increase, '$(', greatest_increase, ')'])
    csvwriter.writerow (['Greatest Decrease in Profits:', month_greatest_decrease, '$(' , greatest_decrease,')'])