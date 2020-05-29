"""Дополнительные подпрограммы, отсутствующие
в установленных сторонних библиотеках.
"""
import numpy

def get_note(freq: float, delay: numpy.ndarray, /) -> numpy.ndarray:
    """Функция формирования нотной последовательности.
    Только позиционные аргументы.
    """
    return numpy.sin(2 * numpy.pi * delay * freq)

def awgn(_loc: float, _scale: float, arr: numpy.ndarray, /) -> numpy.ndarray:
    """Генерация белого шума из переданного массива
    loc - центр нормального распределения,
    scale - ширина отклонения распределения.
    """
    noise = numpy.random.normal(_loc, _scale, arr.size)
    return arr + noise

def quantiz(lbrace, rbrace, x, /):
    """Квантование х по левой или правой границе на основе модуля меньшего расстояния.
    Если расстояние одинаково до двух границ, то функция возвращает левую границу.
    """
    if numpy.abs(rbrace - x) < numpy.abs(lbrace - x):
        res = rbrace
    else:
        res = lbrace
    return res

def dec2bin(dec: int, bitdepth=None) -> str:
    """Перевод чисел из десятичой СС
    в шестандцатиричную, с учётом разрядной сетки
    и без учёта знака числа.
    bitdepth - ширина разрядной сетки.
    """
    bin_num = "{:b}".format(abs(dec))
    if bitdepth is None:
        res = bin_num
    else:
        if (anum:=bitdepth - len(bin_num)) > 0:
            res = '0' * anum + bin_num
        else:
            res = bin_num
    return res

def bit_grid(min_num: int, max_num: int, /) -> int:
    """Определение разрядной сетки для чисел
    со знаком.
    """
    # Начальное приближени размера сетки
    appr = len(dec2bin(max_num))
    grid_size = 2 ** (appr - 1)
    # Расчёт размера сетки
    while not ((min_num in range(-grid_size, grid_size))\
    and (max_num in range(-grid_size, grid_size))):
        appr += 1
        grid_size = 2 ** (appr - 1)
    return appr

def bincodes(nums: tuple, bitdepth=None) -> list:
    """Перевод чисел в дополнительный код.
    """
    compl_arr = []
    # Определение размера разрядной сетки
    grid_size = bit_grid(min(nums), max(nums))
    if bitdepth is None:
        levels = 2 ** grid_size
        bitdepth = grid_size
    else:
        if grid_size >= bitdepth:
            levels = 2 ** grid_size
            bitdepth = grid_size
        else:
            levels = 2 ** bitdepth
    for elm in nums:
        if elm < 0:
            compl_arr.append("{} ({})".format(dec2bin(levels + elm, bitdepth), elm))
        else:
            compl_arr.append("{} ({})".format(dec2bin(elm, bitdepth), elm))
    return compl_arr
