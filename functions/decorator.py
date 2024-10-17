# "==================================================Декораторы============================================="
# # Функция высшего порядка - функция, которая принимает в аргументы другую функцию, создает внутри себя функцию, вызывает функцию, возвращает функцию

# # Декоратор - функция высшего порядка, которая нужна чтобы расширять функционал функции, не изменяя ее функционал (функция обертка)


# # как пишутся декораторы

# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         from datetime import datetime
#         print(f'start: {datetime.now()}')
#         func(*args, **kwargs)
#         print(f'finish: {datetime.now()}')
#     return wrapper

# @time_decorator
# def hello():
#     print('Привет')

# # hello()


# def func_total_time(func):
#     def wrapper(*a, **k):
#         from datetime import datetime
#         now = datetime.now()
#         correct_format = now.strftime('$d.%m,%y,%h,%m')
#         print(f'функция запущена: {correct_format}')
#         func(*a, **k)
#     return wrapper    

# @func_total_time
# def iterate_list(list):
#     for i in list:
#         print(i)


# iterate_list([1,1,1,1,1,1,1])   


# def iter_decorator(num):
#     def inner_decorator(func):
#         def wrapper(*a, **k):
#             for i in range(num):
#                 func(*a, **k)

#         return wrapper
#     return inner_decorator


# @iter_decorator(100)
# def hello():
#     print('hello')

# hello()   


from time import time
import requests





def benchmar(func):
    def wrapper(*a, **k):
        strat = time()
        func(*a, **k)
        finish = time()
        total_time = finish - strat
        print(f'время выполнения функции: {total_time} секунд')
    return wrapper


# @benchmar
# def iter_range():
#     for i in range(1,100001):
#         count = 0
#         count += i
#     print(count)    
# iter_range() 
# 

@benchmar
def fetch_webpage():
    webpage = requests.get('https://youtube.com')

fetch_webpage()    
   
