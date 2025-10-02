#Jacob Fitchwell
#Period 8
#10/1/25

print("Task #1")

full_name = input("What is your first and last name? ")

space = full_name.find(" ")
first_name = full_name[0:space]
last_name = full_name[space: len(full_name)]

print(first_name.title(), last_name.title())

print(first_name[0].lower() + first_name[1:].upper(), last_name[1].lower() + last_name[2:].upper())

print("Task #2")

phrase = 'Once you start down the dark path, forever will it dominate your destiny.'

print(phrase.upper())

phrase2 = phrase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")

print(phrase2)

print("Task #3")

print(len(phrase))

number = len(phrase)

part1 = phrase[:number//3]
part2 = phrase[number//3:number//3 *2]
part3 = phrase[number//3 *2 :]

print(part2)
print(part3)
print(part1)

print("Task #4")

five_numbers = input("Please enter a 5 digit number?")