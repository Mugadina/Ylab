# Импорт необходимых модулей

from functools import reduce
import itertools


# Задача №1. Написать метод domain_name, который вернет домен из url адреса:


def domain_name(url):
    return url.replace("http://", "").replace("https://", "").replace("www.", "").split(".")[0]

# Задача №2. Написать метод int32_to_ip, который принимает на вход 32-битное целое число
# (integer) и возвращает строковое представление его в виде IPv4-адреса:


def int32_to_ip(int32):
    x1 = (int32 // 256**3) % 256
    x2 = (int32 // 256**2) % 256
    x3 = (int32 // 256) % 256
    x4 = int32 % 256
    return str("{}.{}.{}.{}".format(x1, x2, x3, x4))

# Задача №3. Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:


def zeros(n):
    number = 0
    while n > 0:
        number += n // 5
        n //= 5
    return number

# Задача №4. Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.


def bananas(s):
    position_b = [index for index, letter in enumerate(s) if letter == 'b']
    position_a = [index for index, letter in enumerate(s) if letter == 'a']
    position_n = [index for index, letter in enumerate(s) if letter == 'n']

    var_b = itertools.combinations(position_b, 1)
    var_a = itertools.combinations(position_a, 3)
    var_n = itertools.combinations(position_n, 2)

    variants = itertools.product(var_b, var_a, var_n)
    variants = [set(v1 + v2 + v3) for v1, v2, v3 in variants]

    return set([''.join(l if i in v else '-' for i, l in enumerate(s)) for v in variants if ''.join(l for i, l in enumerate(s) if i in v) == 'banana'])

# Задача №5. Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.


def count_find_num(primesL, limit):
    numbers = reduce((lambda a, b: a * b), primesL, 1)
    if numbers > limit:
        return []
    nums = [numbers]
    for i in primesL:
        for n in nums:
            num = n * i
            while (num <= limit) and (num not in nums):
                nums.append(num)
                num *= i
    return [len(nums), max(nums)]
