from math import sqrt
if __name__ == '__main__':
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    c = float(input('Введите c: '))
    if a == 0:
        x = -(c/b)
        print(x)
    else:
        D = b**2 - 4*a*c
        if D == 0:
            x = -b/(2*a)
            print(x)
        elif D < 0:
            print('Корней нет')
        else:
            x1 = -(b - sqrt(D)) / (2 * a)
            x2 = -(b + sqrt(D)) / (2 * a)
            print(x1, x2)
