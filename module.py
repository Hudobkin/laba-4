# my_module.py

def greet(name):
    return f"Привет, {name}!"

def plus(a, b):
    return a + b
def mult(a, b):
    return a * b


def maxelm(lst):
    if not lst:
        return None

    elm = lst[0]
    for element in lst:
        if element >elm:
           elm = element

    return elm


def numsum(number):
    return sum(int(digit) for digit in str(number))


def maxsum(numbers):
    if not numbers:
        return None

    max_sum = 0
    nummax = numbers[0]

    for number in numbers:
        digit_sum = numsum(number)
        if digit_sum > max_sum:
            max_sum = digit_sum
            nummax = number

    return nummax