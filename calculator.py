print("welcom to python Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? (10, 15, 20):"))
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
people = int(input("How many people are splitting the bill?"))
per_person = total_bill / people
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total to pay: ${total_bill:.2f}")
print(f"Each people should pay: ${per_person:.2f}")