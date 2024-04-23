# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################
st = 'as22fooeis81a76'
print(','.join([char for char in st if char.isdigit()]))
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

chars = [char if char.isdigit() else ' ' for char in st]
print(','.join(''.join(chars).split()))
# #################################################################################
# list comprehension
# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
print([ch.upper() for ch in greeting])
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
print([i ** 2 for i in range(50) if i % 2])

# function
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# - створити функцію яка виводить ліст
def show_list(l):
    for i in l:
        print(i, end=' ')


show_list(list)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_number(a, b, c):
    print(f'\n{max(a, b, c)}')
    return max(a, b, c)


max_number(1, 22, 3)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def max_min_number(*args):
    print(max(args))
    return min(args)


max_min_number(1, 23, 4, 534, 3)


# - створити функцію яка повертає найбільше число з ліста
def max_of_list(l):
    return max(l)


# - створити функцію яка повертає найменьше число з ліста
def mim_of_list(l):
    return min(l)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_of_list(l):
    return sum(l)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def avg_of_list(l):
    return sum(l) / len(l)


# ################################################################################################
# 1)Дан list:
list2 = [22, 3, 5, 2, 8, 2, 23, 8, 23, 5]


#   - знайти мін число
def min_of_list():
    print(min(list2))


#   - видалити усі дублікати
def dublicates():
    print(set(list2))


#   - замінити кожне 4-те значення на 'X'
def x_four():
    print(['x' if not (i + 1) % 4 else item for i, item in enumerate(list2)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


square(7)


# 3) вывести табличку множення за допомогою цикла while
def multi_table():
    n = 9
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print(f'{i*j:4}', end='')
            j+=1
        i+=1
        print()
multi_table()
# 4) переробити це завдання під меню
def menu():
    while True:
        print('1. Min')
        print('2. Dublicate')
        print('3. X for four')
        print('4. Square')
        print('5. MultiTable')
        print('0. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            min_of_list()
        elif choice == 2:
            dublicates()
        elif choice == 3:
            x_four()
        elif choice == 4:
            square(7)
        elif choice == 5:
            multi_table()
        elif choice == 0:
            break

menu()