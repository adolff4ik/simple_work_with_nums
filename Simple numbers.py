import math

num1 = input('Введіть число від 0 до 1000:')

num2 = math.trunc(float(num1))

def is_prime (num1):
    if float(num1) == int(num2):
        return True
    else: return False

print(is_prime (num1))
