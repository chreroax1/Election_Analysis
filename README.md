<<<<<<< HEAD
<<<<<<< HEAD
# Election Audit

## Overview of Election Audit

A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election.
=======
# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given you the following talks to complete the election audit of a recent local congressional election
>>>>>>> ba6508a66ca91998da53c48c24c7e18fd902cff6

1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the total number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.

## Resources
<<<<<<< HEAD

-	Data Source: election_results.csv
-	Software: Python 3.7.6, Visual Studio Code, 1.50.1

## Election_Audit Results

=======
-	Data Source: election_results.csv
-	Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
>>>>>>> ba6508a66ca91998da53c48c24c7e18fd902cff6
The analysis of the election show that:
-There were 369,711 votes cast in the election.
-The candidates were:

-	Charles Casper Stockham
-	Diana DeGette
-	Raymon Anthony Doane

- The candidate results were:

-	Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
-	Diana DeGette received 73.8% of the vote and 272,892 number of votes
-	Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes

- The winner of the election was:
-	Diana DeGette who received 73.8% of the vote and 272,892 number of votes.
<<<<<<< HEAD


## Challenge Overview

The election commission requested some additional data to complete the audit:

- The voter turnout for each county.
- The percentage of votes from each county out of the total count.
- The county with the highest turnout. 

Working from the same elections_results.csv file I used for loops and conditional statements with membership and logical operators to find the requested results. 

## Challenge Summary

Working from the same elections_results.csv file I used for loops and conditional statements with membership and logical operators to find the requested results. 

I first initialized a county list, county_options, to hold the names of the counties and initiated a dictionary, county_votes, to hold the county as the key and the votes cast for each county as the values.

county_options = []
county_votes = {}

Then I initialized an empty string, winning_county, to hold the county name and a variable, winning_count, to hold the number of votes of the county that had the largest turnout. 

winning_county = ""
winning_vote_count = 0

After initializing those I wrote a script to get the county name from each row, a decision statement with a logical operator to check if the county name acquired is in the list created earlier and if the county name isn't, add it to the list of county names list and then add to that county's vote count. 

	county_name = row[1]
        	if county_name not in county_options:
            
            	county_options.append(county_name)

            	county_votes[county_name] = 0
        
       	 county_votes[county_name] += 1

Next, I used a repetition statement to get the county from the county dictionary, initialized a variable to hold the county's votes as they are retrieved, create a script that calculates the county's votes as a percentage of the total votes, a print statement that prints the current county, its percentage of total votes and its total votes to the command line as well as to my election_results.txt file.

	for county_name in county_votes:
        
        	C_votes = county_votes.get(county_name)
        	C_vote_percentage = float(C_votes) / float(total_votes) * 100

        	county_results = (
            	f"{county_name}: {C_vote_percentage:.1f}% ({C_votes:})\n")

        	print(county_results)
        
        	txt_file.write(county_results)

        	if (C_votes > winning_vote_count):
            	winning_vote_count = C_votes
            	winning_county = county_name
 
Lastly, I used a print statement to print out the county with the largest turnout and saves that data to my election_results.txt file.

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"Winning Vote Count: {winning_vote_count:,}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    txt_file.write(winning_county_summary)
=======
## Challenge Overview



## Challenge Summary

>>>>>>> ba6508a66ca91998da53c48c24c7e18fd902cff6
=======
<<<<<<< HEAD
# Election Audit

## Overview of Election Audit

A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election.
=======
# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given you the following talks to complete the election audit of a recent local congressional election
>>>>>>> ba6508a66ca91998da53c48c24c7e18fd902cff6

1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the total number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.

## Resources
<<<<<<< HEAD

-	Data Source: election_results.csv
-	Software: Python 3.7.6, Visual Studio Code, 1.50.1

## Election_Audit Results

=======
-	Data Source: election_results.csv
-	Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
>>>>>>> ba6508a66ca91998da53c48c24c7e18fd902cff6
The analysis of the election show that:
-There were 369,711 votes cast in the election.
-The candidates were:

-	Charles Casper Stockham
-	Diana DeGette
-	Raymon Anthony Doane

- The candidate results were:

-	Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
-	Diana DeGette received 73.8% of the vote and 272,892 number of votes
-	Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes

- The winner of the election was:
-	Diana DeGette who received 73.8% of the vote and 272,892 number of votes.
<<<<<<< HEAD


## Challenge Overview

The election commission requested some additional data to complete the audit:

- The voter turnout for each county.
- The percentage of votes from each county out of the total count.
- The county with the highest turnout. 

Working from the same elections_results.csv file I used for loops and conditional statements with membership and logical operators to find the requested results. 

## Challenge Summary

Working from the same elections_results.csv file I used for loops and conditional statements with membership and logical operators to find the requested results. 

I first initialized a county list, county_options, to hold the names of the counties and initiated a dictionary, county_votes, to hold the county as the key and the votes cast for each county as the values.

county_options = []
county_votes = {}

Then I initialized an empty string, winning_county, to hold the county name and a variable, winning_count, to hold the number of votes of the county that had the largest turnout. 

winning_county = ""
winning_vote_count = 0

After initializing those I wrote a script to get the county name from each row, a decision statement with a logical operator to check if the county name acquired is in the list created earlier and if the county name isn't, add it to the list of county names list and then add to that county's vote count. 

	county_name = row[1]
        	if county_name not in county_options:
            
            	county_options.append(county_name)

            	county_votes[county_name] = 0
        
       	 county_votes[county_name] += 1

Next, I used a repetition statement to get the county from the county dictionary, initialized a variable to hold the county's votes as they are retrieved, create a script that calculates the county's votes as a percentage of the total votes, a print statement that prints the current county, its percentage of total votes and its total votes to the command line as well as to my election_results.txt file.

	for county_name in county_votes:
        
        	C_votes = county_votes.get(county_name)
        	C_vote_percentage = float(C_votes) / float(total_votes) * 100

        	county_results = (
            	f"{county_name}: {C_vote_percentage:.1f}% ({C_votes:})\n")

        	print(county_results)
        
        	txt_file.write(county_results)

        	if (C_votes > winning_vote_count):
            	winning_vote_count = C_votes
            	winning_county = county_name
 
Lastly, I used a print statement to print out the county with the largest turnout and saves that data to my election_results.txt file.

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"Winning Vote Count: {winning_vote_count:,}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    txt_file.write(winning_county_summary)
=======
## Challenge Overview



## Challenge Summary

>>>>>>> ba6508a66ca91998da53c48c24c7e18fd902cff6
>>>>>>> a399015e9acf680b6c3ec0117a36195096193dad
