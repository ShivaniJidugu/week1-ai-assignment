import json
import random
from datetime import datetime

name = input("Enter your name: ")
print(f"\nHello, {name}! Welcome to Smart Student Assistant.")

with open("tips.json", "r") as file:
    data = json.load(file)

while True:
    print("\n===== SMART STUDENT ASSISTANT =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tip = random.choice(data["study_tips"])
        print("\nStudy Tip:", tip)

        with open("output.txt", "a") as out:
            out.write(f"Study Tip: {tip}\n")

    elif choice == "2":
        quote = random.choice(data["quotes"])
        print("\nMotivation Quote:", quote)

        with open("output.txt", "a") as out:
            out.write(f"Motivation Quote: {quote}\n")

    elif choice == "3":
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("\nCurrent Date & Time:", current_time)

        with open("output.txt", "a") as out:
            out.write(f"Date & Time: {current_time}\n")

    elif choice == "4":
        print("\nThank you for using Smart Student Assistant!")
        break

    else:
        print("\nInvalid choice. Please try again.")