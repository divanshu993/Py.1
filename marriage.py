gender = int(input("Enter 1 for male or 2 for female: "))
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

if gender == 1:
    if age >= 21:
        print("Boy can marry.")
    else:
        print("Boy cannot marry.")
elif gender == 2:
    if age >= 18:
        print("Girl can marry.")
    else:
        print("Girl cannot marry.")
else:
    print("Invalid gender.")
