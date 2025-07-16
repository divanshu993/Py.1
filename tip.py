bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

each_pay = bill / friends
print("Each person has to pay:", each_pay)

tip_percent = float(input("Enter tip percent (10 to 50): "))

if tip_percent >= 10 and tip_percent <= 50:
    tip_amount = (bill * tip_percent) / 100
    print("Tip amount is:", tip_amount)
    total_bill = bill + tip_amount
    print("Total bill with tip is:", total_bill)
    print("Each person pays with tip:", total_bill / friends)
else:
    print("Invalid tip percent.")
