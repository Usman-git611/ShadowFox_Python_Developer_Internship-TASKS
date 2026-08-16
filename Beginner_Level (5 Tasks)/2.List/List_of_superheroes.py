#List of Superheroes
justice_league =["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

#1:-
members=len(justice_league)
print("Step 1 : Justice league =",justice_league)
print("The number of members are ",members)
#Output :-
    #Step 1 :Justice league = ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern']
    #The number of members are  6

#2:-
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("Step 2: After adding Batgirl and Nightwing:")
print(justice_league)

#Output:
    # Step 2:After adding Batgirl and Nightwing:
    # ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

#3:
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("Step 3 : After moving Wonder Woman to the beginning:")
print(justice_league)

#output: 
    #Step 3 :After moving Wonder Woman to the beginning:
    #['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

#4.
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index , "Green Lantern")

print("Step 4: After moving Green Lantern between Aquaman and Flash:")
print(justice_league)
#output: 
    # Step 4:After moving Green Lantern between Aquaman and Flash:
    # ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Green Lantern', 'Aquaman', 'Batgirl', 'Nightwing']

#5.
justice_league = ["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]

print("Step 5:New Justice League:")
print(justice_league)

#Output: 
# Step 5:New Justice League:
# ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']

#6.
justice_league.sort()

print("Step 6:Alphabetically sorted Justice League:")
print(justice_league)
#output: 
# Step 6:Alphabetically sorted Justice League:
# ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']

#BONUS: 
print("\n BONUS : \n New Leader:", justice_league[0])
