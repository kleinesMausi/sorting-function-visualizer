from util import get_color, make_interface

def initialize_empty_data_grid(data: list[float]) -> list[list[bool]]:
    max_element = max(data)
    return [[False for _ in data] for _ in range(round(max_element))]


def transform_data_to_grid(data: list[float]) -> list[list[bool]]:
    grid = initialize_empty_data_grid(data) 
    max_element = max(data)
    for row_idx, row in enumerate(grid):
        for pixel, value in enumerate(data):

            # "value >= round(max_element) - row_idx", um Daten als balken von unten nach oben zu räpresentieren
            # "value >= row_idx", um Daten als Balken von oben nach unten zu räpresentieren
            if value >= round(max_element) - row_idx: 
                row[pixel] = True
    return grid


def print_data(grid: list[list[bool]], 
               data_tuple: tuple[list[float] | None, list[float] | None] = (None, None),
               data_representation_char:str = "█", 
               information: tuple[bool, list, int] = (False, [], 0)
               ) -> None:
    interface = ""

    should_give_info, element_relations, total_swaps = information
    
    for row in grid:
        for pixel_idx, pixel in enumerate(row):
            if pixel:
                if should_give_info and pixel_idx <= len(element_relations):
                    color_code = element_relations[max(0, pixel_idx - 1)]
                    interface += f"{get_color(color_code)}{data_representation_char}{get_color(None)}"
                else:
                    interface += data_representation_char
            else:
                interface += " "
        interface += "\n"

    if should_give_info:
        interface = make_interface(interface, data_tuple, total_swaps)

    print(interface)

def render(data: list[float], 
           data_tuple: tuple[list[float] | None, list[float] | None] = (None, None),
           information: tuple[bool, 
           list[bool], int] = (False, [], 0)
           ) -> None:
    
    print_data(transform_data_to_grid(data), 
               data_tuple=data_tuple,
               information=information)


if __name__ == "__main__":
    data = [1,2,3.2]
    render(data)