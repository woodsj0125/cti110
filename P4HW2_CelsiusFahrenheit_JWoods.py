#Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents.
#12/2/2018
#CTI -110 P4HW2 - Celsius to Fahrenheit Table
#Javonte Woods

#Print the table headings
print("Celsius\Fahrenheit")
print("______________")


#print the numbers 0 through 20
for number in range (0, 20):
    
    Celsius = int(input(":"))

    Fahrenheit = 9/5 * Celsius + 32
    print(Celsius, '\t', Fahrenheit)
    
