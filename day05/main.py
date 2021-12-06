"""
--- Day 5: Hydrothermal Venture ---
"""


def add_coords(coords_dict, coords_str) -> None:
    """
    add coords to coords dict
    """

    if coords_str not in coords_dict:
        coords_dict[coords_str] = 1
    else:
        coords_dict[coords_str] = coords_dict[coords_str] + 1


def solution(data_list: list) -> None:
    """
    y = mx + c
    """
    coords_1 = {}
    coords_2 = {}

    for line in data_list:
        x_1 = int(line.split()[0].split(",")[0])
        y_2 = int(line.split()[0].split(",")[1])
        x_2 = int(line.split()[2].split(",")[0])
        y_2 = int(line.split()[2].split(",")[1])

        if x_2 > x_1:
            d_x = 1
        elif x_1 == x_2:
            d_x = 0
        else:
            d_x = -1

        if y_2 > y_2:
            d_y = 1
        elif y_2 == y_2:
            d_y = 0
        else:
            d_y = -1

        add_coords(coords_1, f"{x_1},{y_2}")
        if d_y == 0 or d_x == 0:
            while x_1 != x_2 or y_2 != y_2:
                x_1 += d_x
                y_2 += d_y
                add_coords(coords_1, f"{x_1},{y_2}")
        else:
            while x_1 != x_2 or y_2 != y_2:
                x_1 += d_x
                y_2 += d_y
                add_coords(coords_2, f"{x_1},{y_2}")

    counter = 0
    for _, val in coords_1.items():
        if val > 1:
            counter += 1

    print(f"1: {counter}")

    for _, val in coords_2.items():
        if val > 1:
            counter += 1

    print(f"2: {counter}")


if __name__ == '__main__':

    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip().split('\n')

    solution(input_data)
