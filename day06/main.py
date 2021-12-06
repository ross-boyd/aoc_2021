"""
--- Day 6: Lanternfish ---
"""


def solution(fish_timers: list, days: int) -> int:
    """
    how many fish could a lanternfish lantern if a laternfish could latern fish
    """

    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in fish_timers:
        fish_dict[fish] = fish_dict[fish] + 1

    for _ in range(days):

        next_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

        for fish in range(1, 9):

            next_dict.update({fish-1: fish_dict[fish]})

        next_dict.update(
            {6: next_dict[6] + fish_dict[0], 8: next_dict[8] + fish_dict[0]})

        fish_dict = next_dict.copy()

    return sum(fish_dict.values())


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.readline().rstrip().split(',')
    input_data = [int(x) for x in input_data]
    print(f"1: {solution(input_data, 80)} 2: {solution(input_data, 256)}")
