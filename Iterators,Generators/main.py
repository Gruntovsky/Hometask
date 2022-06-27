from data import nested_list
# print(nested_list[0][0])

print()
print('Iterator')
class FlatIterator:
    def __init__ (self,nested_list,start:int,end:int, step:int = 1):
        self.nested_list = nested_list
        self.start = start
        self.end = end
        self.step =  step

    def __iter__(self):
        self.cursor = self.start - self.step
        return self

    def __next__(self):
        self.cursor += self.step
        if self.cursor == len(nested_list):
            raise StopIteration
        return nested_list[self.cursor]



for item in FlatIterator(nested_list,0,len(nested_list)):
     for result in item:
         print(result)

print()
print('Generator')
def FlatGenerator():
    for x in nested_list :
        yield x

a = FlatGenerator()
for x in a:
    for result in x:
        print(result)



