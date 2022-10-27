# 1. спрашивает слово на английском к примеру - abandon
# 2. создает папку с названием abandon в папке dictionaries на рабочем столе
# 3. заходит на сайт playphrase.me > вводит в поиске слов название слова и скачивает первые 5 видео.(1 видео. стоп скачать. 2 видео стоп скачать)
#загружает их в папку abandon 
# 4. В папке abandon создает текстовый файл со списком субтитров из видео(abandon.txt)

import os.path
import os  
import time
import requests
from string import ascii_letters


def new_folder(name):
	try:
		folder = os.mkdir('C:\\yeap\\studying\\dictionary\\A5\\' + name)
	except WindowsError:
		print("Эта папка уже существует")


def check_name(name):
	for i in name:
		if i not in ascii_letters:	
			return False
	return True

flag = False
while flag is False:
	name = input("Введите новое слово для изучения\n") 
	flag = check_name(name)

new_folder(name)


web_name = 'https://playphrase.me/#/search'
web_for_word = 'https://playphrase.me/#/search?q=' + name