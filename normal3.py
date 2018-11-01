a = int(input('a = :'))
b = int(input('b = :'))
c = int(input('c = :'))
D = b**2-4*a*c
if D < 0:
    print('Ответ: Нет действительных корней')
else:
    x1 = (-b+D**0.5)//(2*a)
    x2 = (-b-D**0.5)//(2*a)

    if x2 == x1:
        print('Ответ: ', int(x1), int(x2))
    else:
        print('Ответ: ', int(x1))
