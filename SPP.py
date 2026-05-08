#Q-4
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions.")
else:
    print("Invalid Credentials. Please Try again.")

#Q-5
light = input("Enter the traffic light color: ")

if light == "red":
    print("Wait.")
elif light == "yellow":
    print("Get Ready.")
elif light == "green":
    print("Go.")
else:
    print("Enter a valid traffic light color.")
    
#Q-6
season = int(input("Enter your number: "))

if season == 1:
    print("Spring")
elif season == 2:
    print("Summer")
elif season == 3:
    print("Autumn")
elif season == 4:
    print("Winter")
else:
    print("Enter number between 1-4")

#Q-7
age = int(input("Please enter your age: "))
if not (age>=21 and age<=60):
    print("Your age is not within the range.")
else:
    income = int(input("Please enter your monthly income: "))
    if not (income>=30000):
        print("Your monthy income is less than 30,000.")
    else:
        score = int(input("PLease enter your credit score: "))
        if not (score>=70):
            print("Your credit score is too low.")
        else:
            print("Your Loan has been approved.")

#Q-8
age = int(input("Please enter your age: "))
if age < 12:
    print("The person is under 12, the ticket is free.")
elif age > 60:
    print("The price of ticket for senior is Rs 100. ")
elif (age>12) and (age<60):
    card= input("Do you have a membership card: ")
    if card == "yes":
        print("The ticket cost is Rs 150 for members.")
    elif card == "no":
        print("The ticket cost is Rs 200 for non-members.")
    else:
        print("Please enter yes or no.")
else:
    print("Please enter a valid age.")

#Q-10
radius = int(input("Enter the radius of circle: "))
area = 22/7 * radius * radius
print(f"The area of radius {radius} is {area}.")

#Q-12
num = int(input("Enter any number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

#Q-13
units = float(input("Enter electricity usage (units): "))

if units < 100:
    cost = units * 5

elif units <= 300:
    cost = (100 * 5) + ((units - 100) * 8)

else:
    cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)

print(f"Total electricity bill: Rs {cost}")

#Q-14
player1 = input("Player 1, enter your move (rock, paper, scissors): ").lower()
player2 = input("Player 2, enter your move (rock, paper, scissors): ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

#Q-15
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

#Q-16
total_amount = float(input("Enter total amount: "))
is_member = input("Are you a member? (True/False): ")

if total_amount > 1000 and is_member == "True":
    discount = total_amount * 0.20
    final_amount = total_amount - discount
    print("20% discount applied!")
elif total_amount > 1000 and is_member == "False":
    discount = total_amount * 0.10
    final_amount = total_amount - discount
    print("10% discount applied!")
else:
    final_amount = total_amount
    print("No discount applied.")

print("Final amount: RS", final_amount)

#Q-17
earth_weight = float(input("Enter your Earth weight: "))
print("Planets: 1-Mercury, 2-Venus, 3-Mars, 4-Jupiter, 5-Saturn, 6-Uranus, 7-Neptune")
planet = int(input("Enter planet number: "))

if planet == 1:
    destination_weight = earth_weight * 0.38
    print("Your weight on Mercury is:", destination_weight)
elif planet == 2:
    destination_weight = earth_weight * 0.91
    print("Your weight on Venus is:", destination_weight)
elif planet == 3:
    destination_weight = earth_weight * 0.38
    print("Your weight on Mars is:", destination_weight)
elif planet == 4:
    destination_weight = earth_weight * 2.53
    print("Your weight on Jupiter is:", destination_weight)
elif planet == 5:
    destination_weight = earth_weight * 1.07
    print("Your weight on Saturn is:", destination_weight)
elif planet == 6:
    destination_weight = earth_weight * 0.89
    print("Your weight on Uranus is:", destination_weight)
elif planet == 7:
    destination_weight = earth_weight * 1.14
    print("Your weight on Neptune is:", destination_weight)
else:
    print("Invalid planet number.")

#Q-18
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))

total = m1 + m2 + m3 + m4
percentage = total / 4

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Total Marks:  ", total)
print("Percentage:   ", percentage, "%")
print("Grade:        ", grade)

#Q-19
balance = 5000
correct_pin = 123
is_valid = True

print("Welcome to the ATM.")

if is_valid:
    upin = int(input("Enter your PIN: "))

    if upin == correct_pin:
        print("\n1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        choice = int(input("Select an option (1-3): "))

        if choice == 1:
            amount = float(input("Enter amount to withdraw: RS "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash: RS", amount)
                print("Updated Balance: RS", balance)
            else:
                print("Insufficient balance!")

        elif choice == 2:
            print("Your current balance is: RS", balance)

        elif choice == 3:
            print("Thank you for visiting. Have a nice day!")

        else:
            print("Invalid option selected.")

    else:
        print("Wrong PIN. Access denied.")

else:
    print("Invalid card.")

#Q-20
print("Welcome to the Magic Forest!")


direction = input("\nStage 1: Go North or South? (north/south): ").lower()

if direction == "south":
    print("You went South into the dark woods... GAME OVER!")

elif direction == "north":
    print("You head North into the Magic Forest...")

    
    route = input("\nStage 2: Cross the river or follow the path? (cross/follow): ").lower()

    if route == "cross":
        print("You tried to cross the river but got swept away. Cross the River. END.")

    elif route == "follow":
        print("You follow the path carefully...")

        
        encounter = input("\nYou encounter something! Is it an ogre? (yes/no): ").lower()

        if encounter == "yes":
            print("An Ogre blocks your way! GAME OVER!")

        elif encounter == "no":
            print("The path is clear. You move forward...")

        
            creature = input("\nStage 3: You meet a creature. Choose Fairy, Ogre, or Elf? (fairy/ogre/elf): ").lower()

            if creature == "elf":
                print("The Elf shows you the way out of the Magic Forest. YOU WIN!")

            elif creature == "ogre":
                print("The Ogre attacks you! GAME OVER!")

            elif creature == "fairy":
                print("The Fairy leads you in circles... GAME OVER!")

            else:
                print("Invalid choice. END.")

        else:
            print("Invalid response. END.")

    else:
        print("Invalid choice. END.")

else:
    print("Invalid direction. END.")

#Q-21
floor = int(input("Enter floor number (0-10): "))

if floor < 0 or floor > 10:
    print("Invalid floor.")

else:
    weight = int(input("Enter total weight in lift (kg): "))

    if weight > 500:
        print("Overweight! Lift cannot move.")

    else:
        door = input("Is the door closed? (yes/no): ").lower()

        if door != "yes":
            print("Warning: Close the door.")

        else:
            print("All checks passed. Activating elevator motion!")