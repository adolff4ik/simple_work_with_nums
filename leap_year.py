year = input('Введіть рік:')

def if_year_leap ():
    if int(year)%4==0:
        print('Рік високосний')
    else: print('Рік не високосний')

if_year_leap ()
