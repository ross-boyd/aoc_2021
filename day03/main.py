"""
--- Day 3: Binary Diagnostic ---
"""


def invert_bit(bit):
    """
    return inverted bit
    """
    return int(not bool(bit))


def most_common_bit(data: list, position: int, flag: int) -> list:
    """
    return most common bit data
    """
    average = sum([int(b[position]) for b in data]) / len(data)
    return [round(average), flag][average == 0.5]


def least_common_bit(data: list, position: int, flag: int) -> list:
    """
    return list common bit data
    """
    average = sum([int(b[position]) for b in data]) / len(data)
    return [invert_bit(round(average)), flag][average == 0.5]


def calc_oxygen_reading(data: list) -> int:
    """
    returns o2 reading
    """
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        data = [d for d in data if d[i] == str(
            most_common_bit(data, i, 1))]
    return int(data[0], 2)


def calc_scrubber_reading(data: list) -> int:
    """
    returns co2 scrubber data
    """
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        data = [d for d in data if d[i] == str(
            least_common_bit(data, i, 0))]
    return int(data[0], 2)


def solution(data: list) -> None:
    """
    bits bits bits
    """
    gamma, epsilon = '', ''
    for i in range(len(data[0])):
        average_bit = round(sum([int(b[i]) for b in data])/len(data))
        gamma += str(average_bit)
        epsilon += str(invert_bit(average_bit))
    print(int(gamma, 2)*int(epsilon, 2), calc_oxygen_reading(
        data)*calc_scrubber_reading(data))


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.read().split("\n")
    solution(input_data)
