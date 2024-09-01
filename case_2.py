from datetime import datetime
PATH = "decorator_logs.txt"

# 2. Декоратор из Task_1, но обладающий параметром – путём  к логам
def logging(params):
    def parameterization_decorator(func):
        def wrapper(*args, **kwargs):
            date_time = datetime.now()
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open('main.log', 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return wrapper
    return parameterization_decorator


@logging(PATH)
def shift(steps, lst):
    '''Функкция сдвига в списке чисел на указанное число шагов'''
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return nums

nums = [4, 5, 6, 7, 8, 9, 0]
shift(-2, nums)