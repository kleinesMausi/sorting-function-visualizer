from random import uniform
import argparse
import os

def clearscreen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def get_color(color_code: str|None) -> str:
    color_coding = {
        "r": "\033[91m",  # rot
        "g": "\033[92m",  # grün
        "b": "\033[94m",  # blau
        None: "\033[0m"
    }

    if color_code not in color_coding:
        return ""
    
    return color_coding[color_code]


def get_order(data: list[float], curr_indices :tuple[int, int]) -> list[str]:
    relations = []
    order_broken = False
    
    for i in range(len(data) - 1):

        if i == curr_indices[0] or i == curr_indices[1]:
            relations.append("b")   # färbe getauschte Balken blau
        elif order_broken or data[i] > data[i + 1]:
            relations.append("r")   # färbe nicht sortierten Balken rot
            order_broken = True
        else:
            relations.append("g")   # färbe sortieren Balken grün
    return relations


def get_data(amount_data_points : int = 5, 
             bounds : tuple = (0,10),
             precision: int = 0
             ) -> list[float]:
    
    lower, upper = bounds
    if lower < 0 or upper < 0:
        raise ValueError("Bounds must be non-negative.")

    if lower > upper:
        raise ValueError("Lower bound must be <= upper bound.")

    return [round(uniform(*bounds), precision) for _ in range(amount_data_points)]


def make_interface(data_representation: str = "", 
                   data_tuple: tuple[list[float] | None, list[float] | None] = (None, None),
                   total_swaps: int = 0
                   ) -> str:
    old_data, new_data = data_tuple

    if old_data is None:
        old_data = []
    if new_data is None:
        new_data = []

    template = f'''
Unsorted data   = {old_data}
Sorted data     = {new_data}
Total swaps     = {total_swaps}

{data_representation}
'''.strip()
    
    return template


def parse_args():       # gibts hierfür gute annotation??
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=10)
    parser.add_argument("-d", "--delay", type=float, default=0.1)
    parser.add_argument("-i", "--information", type=bool, default=False)
    parser.add_argument("-p", "--precision", type=int, default=1)
    parser.add_argument("--lower", type=float, default=0.0)
    parser.add_argument("--upper", type=float, default=10.0)
    return parser.parse_args()