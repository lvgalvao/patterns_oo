import random
from typing import List, Callable


def bubble_sort(data: List[int]) -> List[int]:
    data = data.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def quick_sort(data: List[int]) -> List[int]:
    data = data.copy()
    if len(data) <= 1:
        return data
    else:
        pivot = data.pop()
        greater: list[int] = []
        lesser: list[int] = []
        for item in data:
            if item > pivot:
                greater.append(item)
            else:
                lesser.append(item)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


SortFn = Callable[[List[int]], List[int]]


def context(strategy: SortFn, data: List[int]) -> List[int]:
    # multiply every item by 2
    data = [item * 2 for item in data]

    # add a random number
    data = [item + random.randint(-10, 10) for item in data]

    return strategy(data)


def main() -> None:
    print(context(bubble_sort, [1, 5, 4, 3, 2]))
    print(context(quick_sort, [1, 5, 4, 3, 2]))


if __name__ == "__main__":
    main()
