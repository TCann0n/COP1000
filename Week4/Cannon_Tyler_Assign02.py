#Programmer: Tyler Cannon
#Program name: Assignment #02
#Date written: 09/14/2026  
#Purpose: Calculate and display the calculated number and percentages of big cats at the local zoo.

#Part 1, Python code

#inputs

CustomerName = input("Enter your first and last name: ")
Lions = input("Enter the number of Lions: ")
Tigers = input("Enter the number of Tigers: ")

#calculations

Total = Lions + Tigers
PercentLions = Lions / Total
PercentTigers = Tigers / Total

#Prints
print("=" * 60)
print(f"Local Zoo - Big Cats Report: By {CustomerName}")
print("=" * 60)
print(f"Number of Lions: {Lions}")
print(f"Number of Tigers: {Tigers}")
print(f"Total Big Cats: {Total}")
print("=" * 60)
print(f"Lions: {PercentLions}")
print(f"Tigers: {PercentTigers}")
print("=" * 60)