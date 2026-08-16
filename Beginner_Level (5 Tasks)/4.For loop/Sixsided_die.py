import random

six_count = 0
one_count = 0
two_six_count = 0
previous_roll = 0

# Roll the dice 20 times
for i in range(20):
    roll = random.randint(1, 6)
    print("Roll", i + 1, ":", roll)
    if roll == 6:
        six_count += 1
    
    if roll == 1:
        one_count += 1

    if roll == 6 and previous_roll == 6:
        two_six_count += 1

    previous_roll = roll


print("\nStatistics:")
print("Number of times rolled 6:",six_count)
print("Number of times rolled 1:",one_count)
print("Number of times rolled two 6s in a row:",two_six_count)

#Output: 
# Roll 1 : 3
# Roll 2 : 2
# Roll 3 : 6
# Roll 4 : 3
# Roll 5 : 5
# Roll 6 : 1
# Roll 7 : 6
# Roll 8 : 3
# Roll 9 : 3
# Roll 10 : 3
# Roll 11 : 5
# Roll 12 : 5
# Roll 13 : 4
# Roll 14 : 5
# Roll 15 : 2
# Roll 16 : 4
# Roll 17 : 1
# Roll 18 : 6
# Roll 19 : 6
# Roll 20 : 4

# Statistics:
# Number of times rolled 6: 4
# Number of times rolled 1: 2
# Number of times rolled two 6s in a row: 1