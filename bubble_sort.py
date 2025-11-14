from visualizer import render
from util import *
import time


def bubble_sort(inform: bool, 
                delay: float = 0.01, 
                data: list|None = None, 
                print_func = print
                ) -> list[float]:
    
    if data is None:
        data = []

    total_swaps = 0
    for i in range(len(data)):
        swapped = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                total_swaps += 1
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                
                clearscreen()
                print_func(data, information=(inform, get_order(data), total_swaps))
                time.sleep(delay)

        if not swapped:
            break

def main() -> None:
    args = parse_args()
    data = get_data(amount_data_points=args.number)
    bubble_sort(args.information, args.delay, data, render)


if __name__ == "__main__":
    main()