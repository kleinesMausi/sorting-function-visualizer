from random import uniform
import argparse
import os

def clearscreen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def get_order(data: list[float]) -> list[bool]:
    relations = []
    order_broken = False
    
    for i in range(len(data) - 1):
        if order_broken or data[i] > data[i + 1]:
            relations.append(False)
            order_broken = True
        else:
            relations.append(True)
    return relations


def get_data(amount_data_points : int = 5, 
             bounds : tuple = (0,10),
             precision: int = 0
             ) -> list[float]:
    
    return [round(uniform(*bounds), precision) for _ in range(amount_data_points)]

def parse_args():       # gibts hierfür gute annotation??
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=10)
    parser.add_argument("-d", "--delay", type=float, default=0.1)
    parser.add_argument("-i", "--information", type=bool, default=False)
    return parser.parse_args()