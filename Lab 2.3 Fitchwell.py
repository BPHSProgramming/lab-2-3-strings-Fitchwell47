#Jacob Fitchwell
#Period 8
#10/1/25

print("Task #1")

full_name = input("What is your first and last name? ")

space = full_name.find(" ")
first_name = full_name[0:space]
last_name = full_name[space: len(full_name)]

print(first_name.title(), last_name.title())

print(first_name[0].lower() + first_name[1:].upper(), last_name[0].lower() + last_name[1:].upper())