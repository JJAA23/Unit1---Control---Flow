print(" BMI Calculator ")

height = input("Height in inches: ")
weight = input("Weight in pounds: ")

if not height or not weight:
    print("Please enter positive values")
else:
    height = float(height)
    weight = float(weight)

    if height <= 0 or weight <= 0:
        print("Please enter positive values")
    else:
        bmi = round((weight / (height ** 2)) * 703, 1)

        category = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"

        recommendation = "Gain weight" if category == "Underweight" else "Maintain weight" if category == "Normal" else "Lose weight"
        risk = "High" if category == "Obese" else "Moderate" if category == "Overweight" else "Low"

        print("\n=== BMI HEALTH REPORT ===")
        print(f"Height: {height} ")
        print(f"Weight: {weight} lbs")
        print(f"BMI: {bmi} ")
        print(f"Category: {category} ")
        print(f"Recommendation: {recommendation} ")
        print(f"Health Risk: {risk} ")
        print("=========================")
