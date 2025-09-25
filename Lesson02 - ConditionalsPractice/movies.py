age = int(input("Whats your age: "))

if age >= 0:
    if age <= 10:
        print(f"WARNING: Not reccomended for your age!, Rating = PG-13  ")
if age >= 10:
    if age <= 15:
        print("Denied, You must be 17+ to watch this movie. Rating: R ")
    