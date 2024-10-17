"================================================Встроенные функции======================================"
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [10.1, 10.2, 20.6]

# zipped = list(zip(list1, list2, list3))
# print(zipped) # <zip object at 0x1004f3ec0> / [(1, 'a', 10.1), (2, 'b', 10.2), (3, 'c', 20.6)]

# for element in zipped:
#     print(element)

# # (1, 'a', 10.1)
# # (2, 'b', 10.2)
# # (3, 'c', 20.6)


# list4 = [1, 2, 3, 4, 5]
# list5 = ['a','b', 'c', 'd', 'e']
# dict_ = dict(zip(list4, list5))
# print(dict_)

"======================================Enumerate==================================================="
# enumerate - генерирует последовательнось (по дефолту получаем генератор)
# enumerated = enumerate('hello') # <enumerate object at 0x7ff6f6bcb8d0>
# # print(enumerated)

# for el in enumerated:
#     print(el)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# string = 'hello world'
# print(list(enumerate(string[5:]))) #[(0, ' '), (1, 'w'), (2, 'o'), (3, 'r'), (4, 'l'), (5, 'd')]

"=======================================map============================================================="
#map- это функция которая принимает в аргументы функцию и полседовательность
#(записывает в последовательность результат функции в которую передаются элементы последовательносьти)


# поменяйте тип данных элементов list_ со строк на числа
# list_ = ['1', '2',' 3', '4', '5']
# mapped_list = list(map(int,list_))
# print(mapped_list)


# # создать новую последовательность элементы которого квадраты элемента list1
# list1 = [12,13,14,15,16,17]
# mapped_list = list(map(lambda x: x**2, list1))
# print(mapped_list)

# mapped_list2 = [i ** 2 for i in list1]
# print(mapped_list2)

# "=====================================filter=================================================================="
# # filter - Возвращает генератор, с элементами, прошедшими филтр(какое-то условие), принимает в себя функци. и последовательность
# # отфильтровать элементы списка оставить только те что больше 0
# list1 = [1, 0, -2, -3, -4, 5, 10]
# filtered = list(filter(lambda x: x > 0, list1))
# print(filtered)


# list_ = list(range(1, 51))
# filtered = list(filter(lambda x: x % 2 == 0, list_))
# print(filtered)


# users = [
#     {'name': 'nikita', 'age': 12},
#     {'name': 'nastya', 'age': 20},
#     {'name': 'artem', 'age': 19}
# ]
# for user in users:
#     print(user)

# оставить пользователей, которые старше 18

# res = list(filter(lambda user: user['age'] > 18, users))
# print(res)


# result =  [i for i in users if i['age'] > 18]
# print(result)

# result2 = list(filter(lambda user: user['age'] > 18, users))
# print(result2)

"=====================================reduce========================================================"
from functools import reduce

# reduce = принимает функцию и последовательность возвращает 1 результат 
# (передаваемая обязательно должна принимать 2 аргумента)

list1 = list(range(1,101))
result = reduce(lambda x, y: x * y, list1)
print(result)


string = 'hello'
res = reduce(lambda x, y: x + '%' + y, string)
print(res)


# 1) напишите программу которая отбирает слова длина которых больше 7 из исходного списка
list2 = ['hello', 'diana', 'educations']
res_list2 = list(filter(lambda x:  len(x) >7, list2))
print(res_list2)

# 2)  напишите программу которая считает количество четных и нечетных чисел в списке 
# и выводит их количество в формате строки "четные: {колич'ество}, нечетные: {количество}"

list3 = range(1,50)
even_count = len(list(filter(lambda x: x % 2 == 0, list3)))
odd_count = len(list(filter(lambda x: x % 2 != 0, list3)))

res_list2 = f"четные: {even_count}, нечетные: {odd_count}"
print(result)

# 3) напишите программу которая находит самое длинное имя в списке
list4 = ['bishkek', 'italy', 'rome', 'Los-Angele', 'Unitet states']

res_list3 = list(reduce(lambda x,y : x if len(x) > len(y) else y, list4))
print(res_list3)

# 4) Напишите програму которая меняет число на 'fizz' если оно делится на 3,
#  и на строку 'buzz' если не делится, в диапазоне чисел от 1 до 50 включительно
list4 = range(1, 51)
res_list4 = list(map(lambda x: 'fizz' if x % 3 == 0 else 'buzz', list4))
print(res_list4)

# 5) напишите программу которая находит минимальное значение у элемента в списке
list5 = range(1,51)
res_list5 = list(filter(lambda a, b: a if a < b else b, list5), list5)
print(list5)





