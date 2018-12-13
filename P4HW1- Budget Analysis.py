#Write a program that asks the user to enter the amount that he or she has budgeted for a month.It then should loop the prompt for user to enter their expenses for the month and keep running a total.
#12/2/2018
#CTI-110 P4HW1 - Budget Analysis
#Javonte Woods

#Needed Information
expense = 0.0
budget = 0.0
difference = 0.0
expenseTotal = 0.0

total_expense = 0
keep_going = 'y'



#Input Information


budget = float(input("What is your budget for the month?"))
print("Please begin entering the amounts of each of your monthly expenses:")

while keep_going == 'y':
    expense = float(input("Monthly expense amount? $"))
    total_expense = total_expense + expense
    keep_going = input("Do you have any other expenses? (Enter y for yes.)")

#Calculations Module
if total_expense < budget:
    difference = budget - total_expense
    print("You were $", difference, " under budget.")

elif total_expense > budget:
    difference = total_expense - budget
    print("You were $", difference, " over budget.")

else:
    print("You were right on budget. Smart shopping!!!")



     
