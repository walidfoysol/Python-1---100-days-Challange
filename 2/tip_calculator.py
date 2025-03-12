print("Welcome To The Tip Calculator \n")
total_bill = float(input("What was the total bill? $"))
people = float(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to tip? 10, 12 or 15? "))
total_tip = (total_bill*tip_percentage)/100
total_waste = total_bill + total_tip
payment = total_waste / people
payment = round(payment,1)
print("Each person should pay: " + str(payment))