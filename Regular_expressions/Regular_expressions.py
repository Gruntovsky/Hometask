from pprint import pprint
import re

import csv

with open("phonebook_raw.csv",encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

phonebook = dict.fromkeys(contacts_list[0])
book =[]
phone = re.compile('(\+7|8)?\s*\((\d+)\)\s*(\d+)(-|\s)*(\d+)(-|\s)*(\d+)')


for i in range(1,len(contacts_list)):
    res = ' '.join(contacts_list[i])
    phones = str(phone.findall(res))
    print(phones)
    phonebook = dict.fromkeys(contacts_list[0])
    phonebook[contacts_list[0][5]] = phones
    book.append(phonebook)

# print(book)

# result = phone.findall(phonebook)
# print(''.join(result[0]))
# номер телефона









# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
