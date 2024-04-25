# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

from typing import Callable


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add, get = notebook()
add('lox')
print(get())


#
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(num: int):
    st = str(num)
    list = []
    size = len(st)-1
    for i ,char in enumerate(st):
        if char != '0':
            list.append(char+'0'*(size-i))
    return ' + '.join(list)

print(expanded_form(27197))

def decor(func):
    i = 0
    def inner(*args, **kwargs):
        nonlocal i
        i += 1
        print('*'*20)
        print(i)
        func(*args, **kwargs)
        print('*'*20)
    return inner

@decor
def func1():
    print('func1')

func1()
func1()
func1()