# String Indexing and Slicing
word = "Python"
#       012345 (positive indexing)
word[0] # letter p (first character)
word[1] # letter y (second character)
word[5] # letter n (last character)
word[-1] # letter n (last character)
len(word) # length of the string 
word(len(word)-1) #n last character

#String slicing
#====================
word[0:3] # letters pyt (Characters 0,1,2)
word[:3] # letters pyt (Characters 0,1,2) (Exact same thing)
word[2:5] # letters tho (characters 2,3,4)

word[2:6] # letters thon (characters 2,3,4,5)
word[2:len(word)] #thon (Characters 2,3,4,5)
word[2:] #thon (characters 2,3,4,5)

word[-3:] #thon (Characters -3,-2,-1 or 3,4,5)


#Part1-String Iteration Patterns
#Direct Character Iteration\
word = "hello"
for char in word:
    print(char)

#index based iteration
for i in range(len(word)):
    print(f"Character {i}: {word[i]}")
    
#Character Classification
char = input("Press a key")
# Check Character Types using ASCII ranges
if "A" <= char <= "Z":
    print(f"'{char}' is uppercase")
if "a" <= char <= "z":
    print(f"'{char}' is lowercase")
if "0" <= char <= "9":
    print(f"'{char}' is a digit")
    
    
    
if "a" <= char <= "z" or "A" <= char <= "Z":
    print(f"'{char}' is a letter")



    