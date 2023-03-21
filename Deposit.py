deposit = int(input('Розмір вкладу:'))

years = int(input('Кількість років:'))

def bank (deposit, years):
    i = 0
    while i < int(years):
        deposit = float(deposit) + float(deposit / 10)
        print(deposit)
        i += 1
    return deposit

bank (deposit, years)
