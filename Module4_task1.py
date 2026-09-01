# m4 task1_1 - бинарный поиск

def binarysearch2():
    my_massive = list(map(int, input('Введите через пробел целые числа массива в любом порядке: ').split()))
    my_massive.sort()
    import random
    right_answer = random.choice(my_massive)
    low = 0
    high = len(my_massive) - 1
        
    while low <= high:
        mid = (low + high) // 2
        guess = my_massive[mid]
        if guess == right_answer:
            return guess
        elif guess > right_answer:
            high = mid - 1
        else:
            low = mid + 1
    return None