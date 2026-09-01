# Модуль 4 задание 2 - сортировка вставками

def insert_search():
    my_massive = list(map(int, input('Введите через пробел целые числа массива в любом порядке: ').split()))
    
    for i in range(1, len(my_massive)):
        key = my_massive[i] # берем начиная с элемента №1. Элемент 0 уходит влево
        j = i - 1 # т.е. сначала это 0
        
        while j >= 0 and my_massive[j] > key: # т.е. пока элемент слева больше элемента справа
            my_massive[j+1] = my_massive[j]
            j -= 1
            my_massive [j + 1] = key # меняем местами
    return my_massive