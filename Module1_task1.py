# Задача 2 (Модуль 1)

full_circle = 109
speed = int(input('Введите скорость: '))
time = int(input('Введите время поездки: '))
print('Вы остановитесь на отметке ', (speed * time) % full_circle, ' км')