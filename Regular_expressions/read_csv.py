import csv
from pprint import pprint



def container():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        book = []
        for i in range(0, len(contacts_list)):
            a = contacts_list[i]
            for i in range(0, len(a)):
                book.append(a[i])
                phonebook = ','.join(book)
        return phonebook

def keys_():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        book = []
        for i in range(0, len(contacts_list)):
            a = contacts_list[i]
            book.append(a)
    return book

