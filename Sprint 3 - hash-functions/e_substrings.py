"""
E. Подстроки

На вход подается строка. Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.

Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не
превосходит 10 000.

Формат вывода
Выведите натуральное число —– ответ на задачу.

Пример 1
Ввод
abcabcbb

Вывод
3
"""


def max_length_without_repetition(word):
    max_sub_word = ''
    count = 0

    for c in word:
        if c not in max_sub_word:
            max_sub_word += c
        else:
            if count < len(max_sub_word):
                count = len(max_sub_word)
            max_sub_word = max_sub_word[max_sub_word.index(c) + 1:] + c

    return count if count > len(max_sub_word) else len(max_sub_word)


if __name__ == '__main__':
    print(max_length_without_repetition(input()))
