from log import log

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
@log('C:/Users/Gregory/Desktop/py/')
def name_search(doc_n):
  """p - поиск гражданина по номеру документа"""
  for docs_items in documents:
    doc_num = docs_items['number']
    person_name = docs_items['name']
    if doc_n == doc_num:
      print(person_name)
      return person_name
  else:
    print('Такого номера нет')

@log('C:/Users/Gregory/Desktop/py/')
def get_key(directories):
  """g - на какой полке находится документ"""
  value = input('Введите номер документа: ')
  for k,v in directories.items():
    if value in v:
       print('Документ находится на полке №:',k)
       return 'Документ находится на полке №:',k
  else:
       print('Нет такого документа')

@log('C:/Users/Gregory/Desktop/py/')
def search():
  """l - cписок людей в архиве"""
  for docs_items in documents:
         print('{} "{}" "{}"'.format(docs_items['type'], docs_items['number'], docs_items['name']))
         return '{} "{}" "{}"'.format(docs_items['type'], docs_items['number'], docs_items['name'])

@log('C:/Users/Gregory/Desktop/py/')
def add_docs(doc_add):
  """a - Добавляет новые нокументы в documents и кладет на полку.
   если нет указанной полки, команда ее создает и кладет на нее"""
  add = list(doc_add)
  if add[3] not in directories.keys():
    documents.append({'type':add[0],'number':add[1],'name':add[2]})
    directories.setdefault(add[3],list(add[1].split(',')))
  else:
    for i in doc_add[3]:
      documents.append({'type':add[0],'number':add[1],'name':add[2]})
      directories[doc_add[3]].append(add[1])
  print('Документы: ',documents)
  print('Полки: ',directories)
  return 'Документы: ',documents,'Полки: ',directories

def commands():
  get_func=input('Команды p,l,g,a; Введите команду:')
  if get_func == 'g':
     get_key(directories)
  elif get_func == 'p':
    doc_n = input('Введите номер документа гражданина:')
    name_search(doc_n)
  elif get_func == 'l':
        search()
  elif get_func == 'a':
      doc_add=input('Введите через запятую тип,номер,ФИО и номер полки: ').split(",")
      add_docs(doc_add)
  else:
    print('нет такой команды!')

commands()