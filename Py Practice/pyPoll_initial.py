# The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Assign a variable fo rthe file to load and the path
#file_to_load = 'resources/election_results.csv'
# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)

# Close the file.
#election_data.close()

# Import the csv and os modules (Adding our dependencies)
import csv
import os
# Add the filename variable that references the path to election_results.csv
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election_results.csv using the with statement as the filename object, election_data
with open(file_to_load) as election_data:
#print the filename object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n---------------------------------\n")

    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")