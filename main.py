import random
import string
from datetime import datetime, timedelta
import module
def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def passwords(N, K):
    passwords = set()
    while len(passwords) < N:
        password = generate_password(K)
        passwords.add(password)
    return passwords

# Основная часть программы
print("Программа для генерации уникальных паролей")

N = int(input("Введите количество уникальных паролей для генерации: "))
K = int(input("Введите длину пароля: "))

if K <= 0:
    print("Ошибка: длина пароля должна быть положительным числом")
else:
    passwords = passwords(N,K)
    print(f"{N} уникальных паролей длиной {K} символов:")
    for password in passwords:
        print(password)
#________________________________________________________________________________

def exam(num_exams, disciplines):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    times = [f"{hour}:{minute:02}" for hour in range(9, 15) for minute in [0, 30]]

    examsp = []
    for discipline in disciplines:
        day = random.choice(days_of_week)
        time = random.choice(times)
        ticket_number = random.randint(1, 20)

        exam_info = f"Экзамен по дисциплине «{discipline}» состоится в {day} время {time}. Ваш счастливый билет №{ticket_number}"
        examsp.append(exam_info)

    return examsp

print("Программа для определения расписания экзаменов")

num_exams = int(input("Введите количество экзаменов: "))
dis = input("Введите наименования дисциплин через запятую и пробел: ").split(", ")
dis = [discipline.strip() for discipline in dis]

exam_schedule = exam(num_exams, dis)
print("\nРасписание экзаменов:")
for exam in exam_schedule:
    print(exam)

#________________________________________________________________________________


days_until_exam = int(input("Введите количество дней до экзамена: "))

current_date = datetime.now()

exam_date = current_date + timedelta(days=days_until_exam)

print(f"Дата экзамена через {days_until_exam} дней будет: {exam_date.strftime('%d.%m')}")

#_____________________________________________________________________________________________

def luckydate(date):
    return date.day % 4 != 0 and date.weekday() != 0

def findlucky(start_date, n, num_dates):
    lucky_dates = []
    current_date = start_date

    while len(lucky_dates) < num_dates:
        current_date += timedelta(days=n)
        if luckydate(current_date):
            lucky_dates.append(current_date)

    return lucky_dates


start_date_str = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))

start_date = datetime.strptime(start_date_str, "%Y/%m/%d")

lucky_dates = findlucky(start_date, n, 3)

print("Счастливые даты:")
for date in lucky_dates:
    print(date.strftime("%d %B, %A"))


#____________________________________________________________________________


name = input("Введите своё имя: ")
print(module.greet(name))

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
res1 = module.plus(a, b)
print(f" {a} + {b} = {res1}")
res2 = module.mult(a, b)
print(f" {a} * {b} = {res2}")

#-------------------------------------------------------------------------------

n = int(input("Введите размер списка: "))
lst = []
for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    lst.append(num)

elm = module.maxelm(lst)

if elm is not None:
    print(f"Максимальный элемент в списке: {elm}")
else:
    print("Список пустой.")

#_____________________________________________________________________________________

n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

nummax = module.numsum(numbers)

if nummax is not None:
    print(f"Число с максимальной суммой цифр: {nummax}")
else:
    print("Список пустой.")