# Кинотеатр

# Дан массив кресел (один ряд) кинотеатра:
# 0 - кресло сводобно;
# 1 - кресло занято.

# Нужно посадить человека как можно дальше от всех
# и вернуть число равное количеству кресел до ближайщего человека.

# Например:
# 1, 0 ,1, 0, 0, X, 0, 0, 1 -> 2
from math import ceil


def find_seat(seats: list[int]) -> int:
    """
    >>> find_seat([1, 0, 0, 0, 1])
    2
    >>> find_seat([1, 0, 1, 0, 0, 1, 0, 0, 0, 1])
    2
    >>> find_seat([1, 0, 1, 0])
    1
    """

    max_streak = 0
    cur_streak = 0

    for idx, seat in enumerate(seats):
        if seat == 0:
            if not cur_streak:
                cur_streak = 1
            else:
                cur_streak += 1
        else:
            max_streak = max(max_streak, cur_streak)
            cur_streak = 0

    return ceil(max_streak / 2)
