age_input = input("Enter your age: ")
rating = input("Enter movie rating (G, PG, PG-13, R): ")

if age_input == "":
    print("ERROR: Please enter your age")
else:
    age = int(age_input)

    if rating == "G":
        print("APPROVED: You can watch this movie!")
    elif rating == "PG":
        if age >= 6:
            print("APPROVED: You can watch this movie!")
        else:
            print("DENIED: Must be 6+ for PG movies")
    elif rating == "PG-13":
        if age >= 13:
            print("APPROVED: You can watch this movie!")
        else:
            print("WARNING: Not recommended for your age")
    elif rating == "R":
        if age >= 17:
            print("APPROVED: You can watch this movie!")
        else:
            print("DENIED: Must be 17+ for R-rated movies")
    else:
        print("ERROR: Invalid movie rating")