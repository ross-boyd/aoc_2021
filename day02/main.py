"""
--- Day 2: Dive! ---
"""


def solution(data: list) -> None:
    """
    dive, dive, dive
    """
    depth_1, depth_2, horizontal_position, aim = 0, 0, 0, 0

    for command in data:
        # Python 3.10
        match command.split():
            case 'forward', units:
                horizontal_position += int(units)
                depth_2 += aim * int(units)
            case 'up', units:
                depth_1 -= int(units)
                aim -= int(units)
            case 'down', units:
                depth_1 += int(units)
                aim += int(units)

    print(
        f"""
        1: Horizontal {horizontal_position}, depth {depth_1}. Product: {horizontal_position*depth_1}
        2: Horizontal {horizontal_position}, depth {depth_2}. Product: {horizontal_position*depth_2}
        """)

    return


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.read().split("\n")

    solution(input_data)
