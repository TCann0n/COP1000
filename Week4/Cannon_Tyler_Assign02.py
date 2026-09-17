#Programmer: Tyler Cannon
#Program name: Assignment #02
#Date written: 09/14/2026  
#Purpose: Calculate and display the calculated number and percentages of big cats at the local zoo.

#Part 1, Python code

#inputs

#input for customer name
CustomerName = input("Enter your first and last name: ")
#input for the number of lions
Lions = int(input("Enter the number of Lions: "))
#input for the number of tigers
Tigers = int(input("Enter the number of Tigers: "))

#calculations
#Total of Big cats
Total = Lions + Tigers
#Percentage of big cats that are lions
PercentLions = Lions / Total
#Percentage of big cats that are tigers
PercentTigers = Tigers / Total

#Prints
#border
print("=" * 60)
#header display
print(f"Local Zoo - Big Cats Report: By {CustomerName}".center(60))
#border
print("=" * 60)
#number of lions printed
print(f"Number of Lions: {Lions}".center(60))
#number of tigers printed
print(f"Number of Tigers: {Tigers}".center(60))
#total number of big cats printed
print(f"Total Big Cats: {Total}".center(60))
#border
print("=" * 60)
#percentage of big cats that are lions printed
print(f"Lions: {PercentLions:.2%}".center(60))
#percentage of big cats that are tigers printed
print(f"Tigers: {PercentTigers:.2%}".center(60))
#border
print("=" * 60)