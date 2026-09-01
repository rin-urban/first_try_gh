#part3 - task1

def triangle_square():
	sides = input('Введите три стороны треугольника через пробел: ')
	a,b,c = sides.split()
	a,b,c = float(a), float(b), float(c)
	return 'Площадь треугольника со сторонами ' + str(a) + ", " + str(b) + " и " + str(c) + " см равна " + str(round(((a+b+c)*(a+b)*(a+c)*(b+c))**0.5,1)) + " см2."

triangle_square()