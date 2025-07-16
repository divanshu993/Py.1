total = int(input("Enter total water bottles: "))
per_day = int(input("Enter bottles you drink per day: "))

day = 1
while total > 0:
    if total >= per_day:
        total -= per_day
        print("Day", day, ": Drank", per_day, "bottles.", total, "left.")
    else:
        print("Day", day, ": Drank", total, "bottles.", 0, "left.")
        total = 0
    day += 1
4