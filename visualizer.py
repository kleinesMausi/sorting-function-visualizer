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
               data_representation_char:str = "█", 
               information: tuple[bool, list, int] = (False, [], 0)
               ) -> None:
    
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"

    should_give_info, element_relations, total_swaps = information
    
    for row in grid:
        for pixel_idx, pixel in enumerate(row):
            if pixel:
                if should_give_info and element_relations and pixel_idx <= len(element_relations):
                    color = green if element_relations[max(0, pixel_idx - 1)] else red
                    print(f"{color}{data_representation_char}{reset}", end="")
                else:
                    print(data_representation_char, end="")
            else:
                print(" ", end="")
        print()

    if should_give_info:
        print(f"[total swaps: {total_swaps}]")


def render(data: list[float], 
           information: tuple[bool, 
           list[bool], int] = (False, [], 0)
           ) -> None:
    
    print_data(transform_data_to_grid(data), information=information)


if __name__ == "__main__":
    data = [1,2,3.2]
    render(data)