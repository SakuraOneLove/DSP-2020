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

def getComplexDomain(halfdim, scale) -> numpy.ndarray:
    """Doing something...
    """
    a = numpy.arange(-halfdim, halfdim)
    z = numpy.zeros(shape=(2*halfdim, 2*halfdim), dtype=complex)
    for j in numpy.arange(0, 2*halfdim):
        z[j,] = (a+(j-halfdim+2)*1j).astype(complex)
    Z = numpy.zeros(shape=(2*halfdim, 1), dtype=complex)
    for k, n in enumerate(z):
        Z[k][0] = n[0]*scale
    return Z

def wrapTo2Pi(Lambdas):
    """Doing something#2...
    """
    wrapped = Lambdas
    for k, n in enumerate(Lambdas):
        positiveInumpyut = (n > 0)
        wrapped[k] = numpy.mod(n, 2*numpy.pi)
        if n == 0 & positiveInumpyut:
            wrapped[k] = 2*numpy.pi
    return wrapped
    