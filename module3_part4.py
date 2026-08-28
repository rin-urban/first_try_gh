#part4_task1

import json

def registration(login,pswrd):
	login = input('Введите ваш логин:')
	pswrd = input('Введите ваш пароль: ')

	pair = {login:pswrd}

	with open("pairs.txt", "w", encoding="utf-8") as file:
    	json.load(pair, file)