#Q-1
number = int(input("Enter your number: "))

if number >= 1 and number <= 100:
    print("Given number is between 1 and 100")
else:
    print("Given number is not between 1 and 100")

#Q-2
number = int(input("Enter a random number: "))

if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

#Q-3
number = int(input("Enter number between 1 and 12: "))

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
          7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

if number > 12 or number < 1:
    print("Error! Enter valid number!")
else:
    print(months[number])

#Q-4
marks = int(input("Enter your marks: "))

if marks > 80:
    print("Your grade is A")
elif marks >= 60:
    print("Your grade is B")
elif marks >= 50:
    print("Your grade is C")
elif marks >= 45:
    print("Your grade is D")
elif marks >= 25:
    print("Your grade is E")
else:
    print("Your grade is F")

#Q-5
number = int(input("Enter your number: "))

if number % 7 == 0:
    print("It is divisible by 7")
else:
    print("Not divisible by 7")

#Q-6
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
op = input("Enter your operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

#Q-7
salary = int(input("Enter your salary: "))
credit = int(input("Enter your credit score: "))

if salary >= 50000 and credit >= 700:
    print("Eligible")
else:
    print("Not eligible")

#Q-8
num = int(input("Enter your number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(f"Your number is {num}")

#Q-9
char = input("Enter your character: ").lower()

if char in "aeiou":
    print("Your character is a vowel")
else:
    print("Your character is a consonant")

#Q-10
grade = int(input("Enter your marks: "))

if grade >= 90 and grade <= 100:
    print("Grade is A")
elif grade >= 80:
    print("Grade is B")
elif grade >= 70:
    print("Grade is C")
else:
    print("Fail")

#Q-11
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
else:
    print("Adult")

#Q-12
char = input("Enter your character: ")

if char.isalpha():
    if char.isupper():
        print("Uppercase")
    elif char.islower():
        print("Lowercase")
else:
    if char.isdigit():
        print("Digit")

#Q-13
colour = input("Enter colour red, green or yellow: ").lower()

if colour == "red":
    print("Stop")
elif colour == "yellow":
    print("Get Ready")
elif colour == "green":
    print("Go")
else:
    print("Enter a valid colour")

#Q-14
age = int(input("Enter your age: "))
experience = int(input("Enter your experience years: "))

if age > 18 and experience >= 2:
    print("Eligible")
else:
    print("Not eligible")

#Q-15
temperature = float(input("Enter the temperature: "))

if temperature > 30:
    print("It's hot, stay hydrated!")
elif temperature >= 15:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

#Q-16
menu = input("Enter your food (Pizza, Burger, Pasta): ").lower()

if menu == "pizza":
    print("Price: $10")
elif menu == "burger":
    print("Price: $7")
elif menu == "pasta":
    print("Price: $8")
else:
    print("Item not on menu")

#Q-17
height = float(input("Enter your height in feet: "))

if height >= 6:
    print("Selected")
else:
    print("Not selected")

#Q-18
age = int(input("Enter your age: "))

if age >= 18:
    print("Allowed for movie")
else:
    print("Not allowed")

#Q-19
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")

#Q-20
month = int(input("Enter your month number: "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Enter number between 1-12")
