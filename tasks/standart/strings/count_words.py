"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На вход получаем строку, в которой слова разделены пробелами (при условии,
что в начале строки и в конце нет пробелов, а также нет ситуаций,
когда подряд идут несколько пробелов), нужно вернуть количество слов в строке.

ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'hello world' -> 2
- 'hello' -> 1
- '' -> 0
"""


def count_words(str_to_count: str) -> int:
    """Считает количество слов в строке

    :param str_to_count: строка для подсчета слов

    :return: количество слов в строке
    """
    words = str_to_count.split()
    result = len(words)
    return result


if __name__ == '__main__':
    string = input('Введите строку для подсчета слов: ')
    print(f"Количество слов: {count_words(string)}")
