# Write a program that asks the user for their 
# name, age, and location
# and then prints out a personalized message.
# Solution
firstName = input("Enter your firstname: ")
surName = input("Enter your Surname: ")
yourAge = input("Enter your age: ")
location = input("Enter your current location: ")
print(firstName)
print(surName)
print(yourAge)
print(location)
print(f"Hello, my name is {surName} {firstName}.I am {yourAge} years old and live in {location}")