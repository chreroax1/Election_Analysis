counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
#    print(counties[1])

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")

#else:
#    print ('Arapahoe or El Paso is not in the list of counties.')

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")

#else:
#    print ('Arapahoe and El Paso is not in the list of counties.')

#for county in counties:
#    print (county)

for i in range(len(counties)):
    print (counties [i])

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)