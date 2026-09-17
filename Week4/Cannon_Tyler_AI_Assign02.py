
# Author: Tyler Cannon
# Course: COP1000 - Fall 2026
# Assignment #02: Big Cats Exhibit Report

#Part 2, AI Python Code

def main():
    # 1. Input statements to collect user data
    full_name = input("Enter your first and last name: ")
    lions = int(input("Enter the number of lions: "))
    tigers = int(input("Enter the number of tigers: "))

    # 2. Calculation statements
    total_cats = lions + tigers
    percent_lions = lions / total_cats
    percent_tigers = tigers / total_cats

    # 3. Display statements using f-strings and centering
    width = 60
    
    print("=" * width)
    heading = f"Local Zoo - Big Cats Report: By {full_name}"
    print(heading.center(width))
    print("=" * width)
    
    print(f"Number of Lions: {lions}".center(width))
    print(f"Number of Tigers: {tigers}".center(width))
    print(f"Total Big Cats : {total_cats}".center(width))
    
    print("=" * width)
    print(f"Lions: {percent_lions:6.2%}".center(width))
    print(f"Tigers: {percent_tigers:6.2%}".center(width))
    print("=" * width)

if __name__ == "__main__":
    main()