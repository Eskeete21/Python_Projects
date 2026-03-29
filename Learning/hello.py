#storing a name in variable "name"
name = input("Enter your name: ").strip().title()

#Split name first and last
first, last = name.split()

#printing out whats in variable with a hello message
print(f"Hello, Mr.{last}!")

