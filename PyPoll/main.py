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
print(candidates_votes)