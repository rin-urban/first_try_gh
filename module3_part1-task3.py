# part1 - task3

number = str(input('Введите ваше число: '))
number1 = number.replace('-','')
summ_of_digits = 0

for i in number1:
    summ_of_digits+=int(i)

print('Сумма цифр числа ', number, ' равна ', summ_of_digits, end=".")