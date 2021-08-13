print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill + bill / 100 * tip
bill_per_person = "{:.2f}".format(total_bill / people)
print(f"Each person should pay: ${bill_per_person}")

# bill_per_person = round(total_bill / people, 2)
# round() will cut zeros after the dot
# e.g. bill_per_person will store 12.3 instead of 12.30
