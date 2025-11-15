from visualizer import render
from util import *
import time


def bubble_sort(inform: bool, 
                delay: float = 0.01, 
                data: list[float] | None = None, 
                print_func = print
                ) -> list[float]:
    
    if data is None:
        data = []
    unsorted = data.copy()
    total_swaps = 0
    for i in range(len(data)):
        swapped = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                total_swaps += 1
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

                if inform:
                    relations = get_order(data, (j, j + 1))
                else:
                    relations = []
                clearscreen()
                print_func(data, 
                           data_tuple=(unsorted, data),
                           information=(inform, relations, total_swaps))
                time.sleep(delay)

        if not swapped:
            break

    return data

def main() -> None:
    args = parse_args()
    bounds = (args.lower, args.upper)
    data = get_data(amount_data_points=args.number, bounds=bounds, precision=args.precision)
    bubble_sort(args.information, args.delay, data, render)


if __name__ == "__main__":
    main()