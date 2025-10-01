password = input("Enter a password: ")

uppercase_count = lowercase_count = digit_count = special_count = 0
for char in password:
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    elif 'a' <= char <= 'z':
        lowercase_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    elif char != ' ':
        special_count += 1

length_ok = len(password) >= 8
requirements_met = length_ok and uppercase_count > 0 and lowercase_count > 0 and digit_count > 0 and special_count > 0

password_lower = password.lower()

repeated_three = False
for i in range(len(password_lower) - 2):
    if password_lower[i] == password_lower[i+1] == password_lower[i+2]:
        repeated_three = True
        break

sequence_found = None
for i in range(len(password_lower) - 2):
    if ord(password_lower[i+1]) == ord(password_lower[i]) + 1 and ord(password_lower[i+2]) == ord(password_lower[i]) + 2:
        sequence_found = password_lower[i:i+3]
        break

print("PASSWORD ANALYSIS")
print(f'Password: "{password}"')
print(f"Length: {len(password)}")
print(f"Uppercase: {uppercase_count}  Lowercase: {lowercase_count}  Digits: {digit_count}  Special: {special_count}")

print("Requirements:")
print("Length (8+):", "PASSED" if length_ok else "FAILED")
print("Uppercase:", "PASSED" if uppercase_count > 0 else "FAILED")
print("Lowercase:", "PASSED" if lowercase_count > 0 else "FAILED")
print("Digits:", "PASSED" if digit_count > 0 else "FAILED")
print("Special:", "PASSED" if special_count > 0 else "FAILED")

print("Security issues:")
print("Repeated 3+ in a row:", "Yes" if repeated_three else "No")
print("Simple sequence:", sequence_found if sequence_found else "No")

if requirements_met and not repeated_three and not sequence_found:
    final_rating = "STRONG"
elif requirements_met:
    final_rating = "MEDIUM"
else:
    final_rating = "WEAK"

print("FINAL RATING:", final_rating)
