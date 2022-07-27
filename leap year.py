year = input('Введіть рік:')

def if_year_leap ():
    if int(year)%4==0:
        print('true')
    else: print('false')

if_year_leap ()