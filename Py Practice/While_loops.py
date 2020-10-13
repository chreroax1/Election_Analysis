#x = 0

#while x <= 5:
#    print (x)
#    x = x + 1

#numbers = [0, 1, 2, 3, 4,]
#for num in numbers:
#    print (num)

#for num in range(5):
#    print (num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.keys ():
#    print (county)

#for county, voters in counties_dict.items():
#    print ("'key' county has 'value' registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)