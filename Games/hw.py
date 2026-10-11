#Get input from user and store it as an integer in user_num
user_num = int(input("Enter a number "))

#Convert the user_num back to str and print it out to user
print("You entered: " + str(user_num))

#Take user_num and square it
squared_num = (user_num * user_num)

#Take user_num and cube it
cubed_num = (user_num * user_num * user_num)

#Convert back to str and print squared and cubed num out
print(str(user_num) + " square is " + str(squared_num))
print("And " + str(user_num) + " cubed is " + str(cubed_num)+ " !!")

user_num2 = input("Enter a number: ")
print("you entered:  " + user_num2)

sum = int(user_num) + int(user_num2)

print(str(user_num)+ " + " + str(user_num2) + " is " + str(sum))

number = input("number")

print(type(number))