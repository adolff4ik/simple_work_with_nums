season = input('Введіть номер місяця: ')

def show_season ():
    if int(season) < 3 or int(season) == 12:
        result = 'winter'
    elif int(season) < 6:
        result = 'sprin'
    elif int(season) < 9:
        result = 'summer'
    elif int(season) < 12:
        result = 'autumn'
    else: result = 'ti lox'
    print(result)

show_season ()
