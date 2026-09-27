import json

pairs = {}

def registration_1():
    login = input('Введите ваш логин: ')
    pswrd = input('Введите ваш пароль: ')
    pairs[login] = pswrd

    with open("pairs_1.txt", "w", encoding="utf-8") as file:
        json.dump(pairs, file, indent=4)