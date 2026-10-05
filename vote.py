age = int(input("Enter your age: "))

if age < 0 or age > 150:
    print("Invalid age, type again")

elif age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")