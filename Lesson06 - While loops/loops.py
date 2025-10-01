# num = 5
# while num > 0:
# #     print(num)
# #     num -= 1
    
num = 10
total = 0

# while num <= 0:
#     total += num #(total = total + num)
#     num += 1

# print(f"Sum of numbers 1-10: {total }")

# while num <= 10:
#     total += 1
#     if num < 10:
#         print(num, end = "+")
#     else:
#         print(num, end = "=")
#     num += 1
# print(total)
# print()




#Sum of digits
# take a user input as int, and sum the digits of it
number = input("Enter a number: ")
sum = 0
# for char in number:
#     print(f"{char} {type(char)}")
#     sum += int(char)
# print(f"Total {sum}")

i = 0
while i<len(number):
    sum += int(number[i])
    i += 1
print(f"Total {sum}")