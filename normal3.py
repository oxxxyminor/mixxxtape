a = int(input('a = : '))
b = int(input('b = : '))
c = int(input('c = : '))
D = b**2-4*a*c
if D < 0:
    print('Ответ:Нет действительных корней')
else:
    x1 = (-b+D**0.5)//2*a
    x2 = (-b-D**0.5)//2*a
    print('Ответ:',x1,x2)
