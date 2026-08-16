total_jacks=0

for i in range(10):
    print("\nDo 10 jumping jacks.")
    total_jacks+=10
    tired=input("Are you tired? (yes/no): ").lower()
    if tired=="yes"or tired=="y":
        skip=input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip=="yes" or skip=="y":
            print("You completed a total of",total_jacks,"jumping jacks.")
            break

    remaining=100-total_jacks
    print("Jumping jacks remaining:",remaining)

else:
    print("Congratulations! You completed the workout.")


#Output: 

# Do 10 jumping jacks.
# Are you tired? (yes/no): no
# Jumping jacks remaining: 90

# Do 10 jumping jacks.
# Are you tired? (yes/no): yes
# Do you want to skip the remaining sets? (yes/no): no
# Jumping jacks remaining: 80

# Do 10 jumping jacks.
# Are you tired? (yes/no): yes
# Do you want to skip the remaining sets? (yes/no): yes
# You completed a total of 30 jumping jacks.