#CTI-110
#P3HW2- Shipping Charges
#Javonte Woods
#11-26-2018
# Write a program that asks the user to enter the weight of a package and then displays the shipping charges.
#Weight of package| 2pounds<= Rate per pound, $1.50, (Over 2pounds>=6,$3.00,  over 6pounds>=10,$4.00, over 10 > , $4.75

print("Please input weight of package.")
Weight = int(input("Weight of package in Pounds:"))

if Weight <= 2:
    print("You'll be charged $1.50 per pound.")

elif Weight  >=2  and Weight <= 6:
    print("You'll be charged $3.00 per pound.")
elif Weight >= 6 and Weight <= 10 :
    print("You'll be charged $4.00 per pound.")

elif Weight > 10:
    print("You'll be charged $4.75 per pound.")
