#Write a program that asks the user for the number of males and the number of females registered in a class. Program then should display the percentage of males and females in the class.
#12/6/2018
#CTI-110 P2HW2- Male Female Percentage
#Javonte Woods


print("How many Males and Females are located within the facility? So that we may gain an percentage")
males = int(input('Number of Males:'))
females = int(input('Number of females:'))

Totalstudents = males + females

#Calculate them.

Totatlstudents = males + females

malePercentage = ( males / Totalstudents ) * 100
femalePercentage = ( females/ Totalstudents ) * 100

print( "Male Percentage: " + str(malePercentage ) )
print ("Female Percnetage: " + str(femalePercentage ) )
    
