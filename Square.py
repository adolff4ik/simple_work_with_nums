from re import S, X


kub = input('Введіть сторону:')

def kBadrat ():
    S = int(kub)*int(kub)
    P = int(kub)*4
    X = float(2 ** .5)*int(kub)
    print(S,P,X)
    return [S, P, X]

kBadrat ()