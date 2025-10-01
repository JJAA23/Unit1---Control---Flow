text = input("Enter a tex:t")
#initialize counters 
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

#track the first and last character
first_letter = None
last_letter = None

print(f"Analyzing: '{text}'")
print("=" * 40)

#process each character
for char in text:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
        if first_letter is None:
            first_letter = char
        last_letter = char #leep updatign the (last one wins)
    #Wcount uppercase 
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    #Wcount lowercase 
    if 'a' <= char <= 'z':
        lowercase_count_count += 1
    #Count digit
    if '0' <= char <= '9':
        digit_count += 1
        
#display the results
print(f"Total Characters: {total_chars}")
