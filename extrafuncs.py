import numpy

def getNote(freq: float, delay: numpy.ndarray, /) -> numpy.ndarray:
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