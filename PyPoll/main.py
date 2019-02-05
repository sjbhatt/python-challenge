import os
import csv

election_csv = os.path.join(".","election_data.csv")

# Open and read csv
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Index tracking for csv file for each line
    total_number_of_votes = 0
    candidate_list = []
    
    # Read through each row of data after the header for couting total number of votes
    for row in csvreader:
        total_number_of_votes += 1
        # Adding unique names to the candidate list
        new_candidate = row[2]
        if new_candidate not in candidate_list:
            candidate_list.append(row[2])
        
    # Creating 2 empty lists
    total_votes_per_candidate = []
    percent_votes_per_candidate = []

    # Counting Votes per each Candidate
    for candidate in candidate_list:
        vote_per_candidate = 0
        csvfile.seek(0) # Resetting the csv iterator for each candidate
        for row in csvreader:
            if candidate == row[2]:
                vote_per_candidate+=1
        percent = (vote_per_candidate/total_number_of_votes)*100
        
        # Appending the results per each candidate
        total_votes_per_candidate.append(vote_per_candidate)
        percent_votes_per_candidate.append(format(percent, '.3f')+'%')

    # Finding the Winner
    winner_candidate_votes = 0
    for i in range(len(total_votes_per_candidate)):
        if winner_candidate_votes < total_votes_per_candidate[i]:
            winner_candidate_votes = total_votes_per_candidate[i]
            winner_candidate_name = candidate_list[i]

    # Lists formatted to include ":" & "()"
    formatted_candidate_list = []
    formatted_total_votes_per_candidate = []
    
    for i in range(len(total_votes_per_candidate)):
        name = candidate_list[i] + str(":")
        formatted_candidate_list.append(name)

        vote_count = str("(") + str(total_votes_per_candidate[i]) + str(")")
        formatted_total_votes_per_candidate.append(vote_count)

    # Writing to a Text File
    # Zip all three lists together into tuples
    results = zip(formatted_candidate_list, percent_votes_per_candidate, formatted_total_votes_per_candidate)
    
    # save the output file path
    output_file = os.path.join("election_results.txt")

    # open the output file, create a header row, and then write the zipped object to the txt
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile, delimiter=' ')

        writer.writerow(["Election Results"])
        writer.writerow(["----------------------------"])
        writer.writerow(["Total Votes:", total_number_of_votes])
        writer.writerow(["----------------------------"])
        writer.writerows(results)
        writer.writerow(["----------------------------"])
        writer.writerow(["Winner:", winner_candidate_name])
        writer.writerow(["----------------------------"])

    # Printing to the Terminal Window
    print ("Election Results")
    print ("----------------------------")
    print ("Total Votes:", total_number_of_votes)
    print ("----------------------------")
    for i in range(len(candidate_list)):
        print (candidate_list[i] + ': ' + str(percent_votes_per_candidate[i]) + ' (' + str(total_votes_per_candidate[i]) + ')')
    print ("----------------------------")
    print ("Winner:", winner_candidate_name)
    print ("----------------------------")