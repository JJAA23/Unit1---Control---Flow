age = 25 
status = "adult" if age >= 18 else "minor" 
score = 75 
message = "Excellent" if score >= 90 else "Keep Trying!" 
password = "mypass123" 
strength = "none fr"
print(f"Password:{password}/nStrength:{strength}")


#Combining Theory + Chaining
category = ("Child" if 0 <= age <= 12 else 
            "teen" if 13 <= age <= 17 else
            "Adult" if 18 <= age <= 64 else
            "old boy"
            )

score = 89
grade = ("A" if 100 <= score <= 97 else 
        "B" if  85 <= score <= 82 else
        "C" if 75 <= score <= 78 else 
        "D"
         )