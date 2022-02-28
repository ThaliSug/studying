# '''Iterator in python is an object that is used to iterate over iterable 
# objects like lists, tuples, dicts, and sets. The iterator object is 
# initialized using the iter() method. It uses the next() method for iteration.'''


# # Here is an example of a python inbuilt iterator
# # value can be anything which can be iterate
# iterable_value = 'Studies'
# iterable_obj = iter(iterable_value)
 
# while True:
#     try:
 
#         # Iterate by calling next
#         item = next(iterable_obj)
#         print(item)
#     except StopIteration:
 
#         # exception will happen when iteration will over
#         break


# # A simple Python program to demonstrate
# # working of iterators using an example type
# # that iterates from 10 to given value
 
# # An iterable user defined type
# class Test:
 
#     # Constructor
#     def __init__(self, limit):
#         self.limit = limit
 
#     # Creates iterator object
#     # Called when iteration is initialized
#     def __iter__(self):
#         self.x = 10
#         return self
 
#     # To move to next element. In Python 3,
#     # we should replace next with __next__
#     def __next__(self):
 
#         # Store current value ofx
#         x = self.x
 
#         # Stop iteration if limit is reached
#         if x > self.limit:
#             raise StopIteration
 
#         # Else increment and return old value
#         self.x = x + 1;
#         return x
 
# # Prints numbers from 10 to 15
# for i in Test(15):
#     print(i)
 
# # Prints nothing
# for i in Test(5):
#     print(i)
    
# # other way:

# # to create your own interator class:
# class ListIterator:
#     # to take any type of object: list
#     def __init__(self, list):
#         self.__list = list
#         self.__index = -1   # starts at -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.__index += 1  # add 1
#         return self.__list[self.__index]  #return the value at the current index

# a = [1,2,3,8,45]
# mylist = ListIterator(a)
# it = iter(mylist)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

class ListIterator_equal:
    # to take any type of object: list
    def __init__(self, list):
        self.__list = list
        self.__index = -1   # starts at -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1  # add 1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]  #return the value at the current index

a = [1,2,3,6,5,4]

mylist  = ListIterator_equal(a)
it = iter(mylist)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))