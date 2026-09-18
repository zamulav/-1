import random

print("Завдання 1")
name = input("Введіть ваше ім'я: ")
age = input("Введіть ваш вік: ")
print(f"Привіт {name}, тобі {age}!")

print("Завдання 2")
check_age = int(input("Введіть ваш вік: "))
if check_age >= 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

print("Завдання 3")
secret_number = random.randint(1, 10)
attempts = 3
print("Я загадав число від 1 до 10. У тебе є 3 спроби!")
for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}: Введіть число: "))
    if guess == secret_number:
        print("Вітаю! Ти вгадав!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Бльше")
else:
    print(f"Ти програв! Я загадав число: {secret_number}")

print("Завдання 4")
start = int(input("Введіть початкове число (з): "))
end = int(input("Введіть кінцеве число (по): "))
for number in range(start, end + 1):
    print(number, end=" ")
print()

print("Завдання 5")
n_even = int(input("Введіть число n: "))
for number in range(n_even, 0, -1):
    if number % 2 == 0:
        print(number, end=" ")
print()

print("Завдання 6")
n_fact = int(input("Введіть число n для обчислення факторіала: "))
factorial = 1
for i in range(1, n_fact + 1):
    factorial *= i
print(f"Факторіал числа {n_fact} дорівнює: {factorial}")

print("Завдання 7")
score = int(input("Введіть кількість балів (0-100): "))
if 0 <= score <= 49:
    print("Незадовільно")
elif 50 <= score <= 69:
    print("Задовільно")
elif 70 <= score <= 89:
    print("Добре")
elif 90 <= score <= 100:
    print("Відмінно")
else:
    print("Помилка: введіть бали від 0 до 100.")

print("Завдання 8")
a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть математичну дію (+, -, *, /): ")
if operation == "+":
    print(f"Результат: {a + b}")
elif operation == "-":
    print(f"Результат: {a - b}")
elif operation == "*":
    print(f"Результат: {a * b}")
elif operation == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(f"Результат: {a / b}")
else:
    print("Помилка: ділити на нуль не можна.")
