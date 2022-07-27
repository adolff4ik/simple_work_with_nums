n = int(input('Розмір вкладу:'))

years = int(input('Кількість років:'))

def bank (n, years):
    i = 0
    while i < int(years):
        n = float(n) + float(n / 10)
        print(n)
        i += 1
    return n

bank (n, years)
