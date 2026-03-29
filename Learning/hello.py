#Keep asking user for gender until a valid gender is input
while True:
    gender = input("What is your gender (Male or Female): ").title().strip()
    if gender == "Male" or gender == "Female":
        break
    print("Please choose a gender! ")

#Keep asking user for first and last name until at least two names are input
while True:
    name = input("Enter your first and last name: ").strip().title()

    #splits name into two parts
    parts = name.split()

    #sets variable first and last to parts[0] and parts[1], so first name = parts[0] and last name = parts[1]
    if len(parts) >= 2:
        first, last = parts[0], parts[1]
        break
    print("Please enter first and last name!")

#printing out last name with hello message 

if gender == "Female":
    print(f"Hello, Ms.{last}!")
else:
    print(f"Hello, Mr.{last}!")



