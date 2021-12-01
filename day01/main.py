"""
Sonar Sweep
"""


def solution(input_data: list, win_size: int) -> int:
    """
    win_sized-measurement sliding window
    """
    increase, index = 0, 0

    while index+1 < len(input_data):
        try:
            if sum(input_data[index+1:index+1+win_size]) > sum(input_data[index:index+win_size]):
                increase += 1
        except IndexError:
            pass
        index += 1
    print(
        f"Number of {win_size} sized windows larger than previous: {increase}")

    return increase


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as file:
        data = file.read().split("\n")
    data = [int(x) for x in data]

    solution(data, 1)
    solution(data, 3)
