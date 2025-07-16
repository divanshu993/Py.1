def is_adult(age):
    return age >= 18

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
roll_number = input("Enter your roll number: ")
address = input("Enter your address: ")

# Check if adult
adult_status = is_adult(age)

# Output
print("Name:", name)
print("Age:", age)
print("Roll Number:", roll_number)
print("Address:", address)
print("Adult:", adult_status)
