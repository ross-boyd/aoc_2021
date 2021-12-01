def solution(data: list, win_size: int) -> int:
    """win_sized-measurement sliding window"""
    increase, x = 0, 0

    while x+1 < len(data):
        try:
            if(sum(data[x+1:x+1+win_size]) > sum(data[x:x+win_size])):
                increase += 1
        except:
            pass
        x += 1
    print(
        f"Number of {win_size} sized windows larger than previous: {increase}")

    return increase


if __name__ == "__main__":

    with open("input.txt", "r") as file:
        data = file.read().split("\n")
    data = [int(x) for x in data]

    solution(data, 1)
    solution(data, 3)
