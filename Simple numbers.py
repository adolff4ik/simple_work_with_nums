import math

num = input('Введіть число від 0 до 1000:')

num2 = math.trunc(float(num))

def is_prime (num):
    if float(num) == int(num2):
        return True
    else: return False

print(is_prime (num))