# ========================================
# ACCELERATED PYTHON UNIT 2 - LESSON 1
# Conditionals: JavaScript to Python
# ========================================

# ========================================
# SECTION 1: QUICK TRANSLATION CHALLENGE
# ========================================
print("==Grade Classification==")
score = 87
if score >= 90:
    print("A grade! get a plus")
elif score >= 80:
    print("B grade!, youre lowkey mid")
else: 
    print("U failed bud")
# ========================================
# SECTION 2: AGE CATEGORY CLASSIFIER
# ========================================
age = (input("Whats your age?"))
if age >= 0:
   if age <= 12:
    print("You are a child")
elif age >= 13:
    print("You are a teenager")
elif age >= 20:
    print("You are an Adult")

    
age = 17
gpa = 3.8
has_license = True
can_drive = age >= 16 and has_license
honor_roll = gpa >= 3.5
eligible = can_drive and honor_roll and age >= 17

print(f"Can Drive: {can_drive}")
print(f"Honor Roll: {honor_roll}")
print(f"Eligible: {eligible}")

if eligible: 
    print("You can pass")


# ========================================
# SECTION 3: STUDENT STATUS CHECKER
# ========================================


# ========================================
# SECTION 4: GRADE VALIDATOR CHALLENGE
# ========================================


# ========================================
# SECTION 5: WEATHER DECISION SYSTEM
# ========================================
