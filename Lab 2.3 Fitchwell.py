print("Task #1")

full_name = input("What is your first and last name? ")

#this is hard coded,  What if you use a differen first and last name. How do you find the blank space?
first_name = full_name[0:5]
last_name = full_name[6:15]

print(first_name.title(), last_name.title())