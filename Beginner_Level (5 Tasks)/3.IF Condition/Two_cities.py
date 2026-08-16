Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

#Find country of first city
if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
elif city1 in India:
    country1 = "India"
else:
    country1 = "Unknown"

#Find country of second city
if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
elif city2 in India:
    country2 = "India"
else:
    country2 = "Unknown"


if country1 == country2 and country1 != "Unknown":
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")

#Output:
# Enter the first city: Mumbai
# Enter the second city: Delhi
# Both cities are in India

# Enter the first city: Mumbai
# Enter the second city: Ajman
# They don't belong to the same country