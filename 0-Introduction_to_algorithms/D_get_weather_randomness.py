"""
D. Хаотичность погоды

Метеорологическая служба вашего города решила исследовать погоду
новым способом.

Под температурой воздуха в конкретный день будем понимать максимальную
температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней,
в которые температура строго больше, чем в день до (если такой существует)
и в день после текущего (если такой существует). Например, если за 5 дней
максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов, то
хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные
условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот
период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.

Формат ввода
В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105.
Во второй строке даны n целых чисел –— значения температуры в каждый из n
дней. Значения температуры не превосходят 273 по модулю.

Формат вывода
Выведите единственное число — хаотичность за данный период.

Пример 1
Ввод
7
-1 -10 -8 0 2 0 5
Вывод
3
"""

from typing import List

from ..timing import timing


@timing
def get_weather_randomness(temperatures: List[int]) -> int:
    temp = [min(temperatures)-1] + temperatures + [min(temperatures) - 1]
    return len(
        [n for n in range(1, len(temp)) if temp[n-1] < temp[n] > temp[n+1]]
    )


@timing
def read_input() -> List[int]:
    _ = int(input())
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    print(get_weather_randomness(read_input()))
