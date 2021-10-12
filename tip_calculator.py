# Make a python script  tip_calculator.py that takes a user's input at the command line for:

# Cost of the food
# Number of people splitting the bill
#  Percentage of the tip
# Hint: you might want to use the input() function for taking user input

# Then, the script should output:

# The total bill (including tip)
# how much each person should pay (you can assume all people will split the bill evenly)
# Assume there is a 10% sales tax. Don't forget to add this into the total bill! 

# Note: your tip calculator should be able to handle a bill of any amount 
# of many money, with any number of people splitting the bill, and with any tip percentage (including 0 tip)

print('tip_calculator')

print()

#Asking for the total cost or the meal?
total_cost = float(input('Total cost of meal without tip $'))

print()
#Asking for the tip in %
total_tip = int(input('what % tip like to give?'))

print()

#Asking how many adults
num_adults = int(input('How many adults?'))

print()

tip_percent = total_tip /100
total_tip_amount = round(total_cost * tip_percent)
total_bill = round(total_tip_amount + total_cost)
bill_per_person = round (total_bill/ num_adults)
bill_to_pay = round(bill_per_person)


print(f'the meal cost with tip $ {total_bill}')

print()

print(f'each have to pay $ {bill_to_pay}')