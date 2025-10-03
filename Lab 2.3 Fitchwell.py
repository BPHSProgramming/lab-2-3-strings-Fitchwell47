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

num_str1 = five_numbers[0]
num_str2 = five_numbers[1]
num_str3 = five_numbers[2]
num_str4 = five_numbers[3]
num_str5 = five_numbers[4]

num_int1 = int(num_str1)
num_int2 = int(num_str2)
num_int3 = int(num_str3)
num_int4 = int(num_str4)
num_int5 = int(num_str5)

sum = num_int1 + num_int2 + num_int3 + num_int4 + num_int5

print(num_str1, "+", num_str2, "+", num_str3, "+", num_str4, "+", num_str5, "=", sum)

print("Task #5")

phrase3 = "Why, you stuck-up half-witted scruffy-looking nerf herder."

print(phrase3[::2])
print(phrase3[::-2])