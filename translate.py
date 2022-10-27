#обходит каталог, создает список из кортежей (имя каталога на английском, имя каталога переведенное на русский )
# закидывает 0 значение кортежа в Excel документы в раздел слова , 1 значение в раздел перевод.
import os
import openpyxl
from googletrans import Translator

def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))


file_name = os.listdir('C:\\Users\\Admin\\Desktop\\dictionary\\A3')
tup_of_words = []
for i in file_name:
    tup_of_words.append(os.listdir('C:\\Users\\Admin\\Desktop\\dictionary\\A3\\' + i))

new = flatten(tup_of_words)

new = [i.replace(".mp4","").replace('-', ' ').title() for i in new]

text = new  
translator = Translator()
translated = translator.translate(text,src='en', dest="ru")

dic = []

for trans in translated:
    a,b = trans.origin,trans.text
    dic.append((a,b))

file_name = 'A3.xlsx'
wb = openpyxl.load_workbook(file_name)
list_of_file = wb['Sheet1']

for k,v in enumerate(dic):
    list_of_file['C' + str(k+2)] = dic[k][0]
    list_of_file['D' + str(k+2)] = dic[k][1]


wb.save(file_name)
wb.close()
print('Готово')




