print("General Knowledge Quiz")
print("Y to start or N to quit")
choice = input("Enter your choice: ")

def start():
    score = 0
    print("What is the captial of Germany")
    ans = (input("Enter Answer: "))
    if ans == "Berlin":
        score += 1

    print("Which country was the first to grant women the right to vote")
    ans = (input("Enter Answer: "))
    if ans == "New Zealand":
        score += 1
    else:
        score -= 1

    print("What is the smallest bone in the human body")
    ans = (input("Enter Answer: "))
    if ans == "Stapes":
        score += 1
    else:
        score -= 1

    print("Which element has the atomic number 79")
    ans = (input("Enter Answer: "))
    if ans == "Gold":
        score += 1
    else:
        score -= 1

    print("Who gifted the statue of liberty to USA")
    ans = (input("Enter Answer: "))
    if ans == "France":
        score += 1
    else:
        score -= 1

    print("What is the name of the first artifical satellite")
    ans = (input("Enter Answer: "))
    if ans == "Sputnik 1":
        score += 1
    else:
        score -= 1

    print("Which is the most abundant element in Earth's crust")
    ans = (input("Enter Answer: "))
    if ans == "Oxygen":
        score += 1
    else:
        score -= 1

if choice == "Y":
    start()


