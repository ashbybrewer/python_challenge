import csv

#inititalize list to store csv data in 
data= []


#open csv file
with open('Resources/election_data.csv', 'r') as file:
    reader=csv.reader(file)
    header=next(reader)# This reads the first line (header) and moves to the next line
    for row in reader:
        data.append(row)
    
#total number of votes 
total_votes=len(data)

#list of candidates and their vote counts using dictionary 
candidates_votes = {}

for row in data:
    candidate_name = row[2]
    if candidate_name not in candidates_votes:
        candidates_votes[candidate_name] = 1  # If the candidate wasn't in our dictionary, add them with 1 vote
    else:
        candidates_votes[candidate_name] += 1  # If they were, increment their vote count

#percentage of votes for each candidate 
candidates_percentages ={}
for candidate, votes in candidates_votes.items():
    percentage=(votes/total_votes)*100
    candidates_percentages[candidate]=percentage

#determine winner
winner = max(candidates_votes, key=candidates_votes.get) 

#print and export outcomes:
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate in candidates_votes:
    results += f"{candidate}: {candidates_percentages[candidate]:.3f}% ({candidates_votes[candidate]})\n"
    
results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

# Print to terminal
print(results)

# Export to text file
with open('analysis/results.txt', 'w') as output_file:
    output_file.write(results)
