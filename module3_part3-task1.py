#part3 - task1

sides = input('Введите три стороны треугольника через пробел: ')
a,b,c = sides.split()
a,b,c = float(a), float(b), float(c)

print('Площадь трегуольника со сторонами ', a,", ", b," и ", c, " см равна ", round(((a+b+c)*(a+b)*(a+c)*(b+c))**0.5,2), "см2." )