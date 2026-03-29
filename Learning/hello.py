while True:
    gender = input("What is your gender (Male or Female): ").title().strip()
    if gender == "Male" or gender == "Female":
        break
    print("Please choose a gender! ")

#storing a name in variable "name"
name = input("Enter your name: ").strip().title()

#Split name first and last
first, last = name.split()

#printing out whats in variable with a hello message

if gender == "Female":
    print(f"Hello, Ms.{last}!")
else:
    print(f"Hello, Mr.{last}!")



