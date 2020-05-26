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
