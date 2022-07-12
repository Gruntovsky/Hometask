from data import nested_list
from itertools import chain

print()
print('Iterator')


class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = -1  # курсор основного списка
        self.nested_list_cursor = 0  # курсор списка вложенного в основной список
        return self

    def __next__(self):
        self.main_list_cursor += 1
        if self.main_list_cursor == len(self.main_list[self.nested_list_cursor]):
            self.main_list_cursor = 0
            self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.main_list):
            raise StopIteration
        return self.main_list[self.nested_list_cursor][self.main_list_cursor]

if __name__ == '__main__':
    flat_list = []
    for item in FlatIterator(nested_list):
        flat_list.append(item)
    print(flat_list)

print()
print('Generator')
def FlatGenerator(nested_list):
    for x in nested_list:
        yield x

a = FlatGenerator(nested_list)
for x in a:
    for result in x:
        print(result)




