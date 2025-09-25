# Three forms of range function

#1 range(Stop) 0,1,2,3,4
for i in range (5):
    print(i)
#2 range(Start, Stop) = 3,4,5,6,7
for i in range (3,8):
    print(i)
#3 range(Start, Stop) = 2,4,6,8,10
for i in range (2,11,2):
    print(i)
#Counting backwards = 10, 8, 6, 4, 2
for i in range(10,1,-2): 
    print(i)

# #countdown timer
# for i in range(10,0,-1):
#     print(int("seconds: " + i))


#countdown timer
import time
for seconds in range(10,-1,-1):
    print(f"{seconds}-seconds")
    # time.sleep(1)  # Wait 1s between numbers
print("Blast off  ")

#Multiplication Table
#Take user inputfor the number and print the table numberx1 = number '

number = int(input("Give me a number between 1 and 12: "))
if number <= number <= 12:
    for i in range(1,13):
        result = number * i
        print(f"{number}x{i:2d} = {result:3d}")
else:
    print("Please enter a number between 1-12")
    

