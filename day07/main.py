"""
--- Day 7: The Treachery of Whales ---
"""
import sys


def solution(crab_positions: list, constant_fuel: bool) -> int:
    """
    v-=-V
    there's probably a better way to do this...
    """
    pos_max = max(crab_positions)
    pos_min = min(crab_positions)
    min_fuel = sys.maxsize

    for position in range(pos_min, pos_max+1):
        steps = fuel = 0
        for crab_pos in crab_positions:
            steps = 0
            steps = abs(crab_pos - position)
            if constant_fuel:
                fuel += steps
            else:
                fuel += (steps*(steps+1))//2
        min_fuel = min(fuel, min_fuel)

    return min_fuel


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.readline().rstrip().split(',')
    input_data = [int(x) for x in input_data]
    print(f"1: {solution(input_data, True)}, 2: {solution(input_data, False)}")
