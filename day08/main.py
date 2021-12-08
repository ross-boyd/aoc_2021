"""
--- Day 8: Seven Segment Search ---
"""


def solution(signal_notes: list) -> tuple:
    """
    returns tuple (part1, part2)
    there's also got to be a nicer way...
    """

    counter = 0
    output_sum = 0
    for note in signal_notes:
        signal_patterns, output_values = note.split(
            " | ")[0], [note.split(" | ")[1]]
        signal_patterns = ["".join(sorted(s))
                           for s in signal_patterns.split(" ")]
        output_values = ["".join(sorted(v))
                         for v in output_values[0].split(" ")]

        crib_sheet = {}
        unknown_signal_patterns = []

        for signal in signal_patterns:
            # Check if the digit is known from the length of the signal
            if len(signal) in [2, 3, 4, 7]:
                match len(signal):
                    case 2:
                        crib_sheet[1] = signal
                    case 3:
                        crib_sheet[7] = signal
                    case 4:
                        crib_sheet[4] = signal
                    case 7:
                        crib_sheet[8] = signal
            else:
                unknown_signal_patterns.append(signal)

        for signal in unknown_signal_patterns:

            # All remaining signals are 2,3,5 or 0,6,9
            if len(signal) == 5:
                # Signal is 2,3 or 5
                if len(list(set(crib_sheet[7]).intersection(signal))) == 3:
                    crib_sheet[3] = signal
                else:
                    # 2 or 5
                    if len(list(set(crib_sheet[4]).intersection(signal))) == 3:
                        crib_sheet[5] = signal
                    else:
                        crib_sheet[2] = signal
            elif len(signal) == 6:
                # Signal is 0, 6 or 9
                if len(list(set(crib_sheet[4]).intersection(signal))) == 4:
                    crib_sheet[9] = signal
                else:
                    # 0 or 6
                    if len(list(set(crib_sheet[7]).intersection(signal))) == 3:
                        crib_sheet[0] = signal
                    else:
                        crib_sheet[6] = signal
            else:
                return 0, 0

        # Reverse the crib_sheet to pattern: digit, and sort the patterns for easier matching
        crib_sheet = {v: k for k, v in crib_sheet.items()}

        # Now, go through the output, lookup the combinations in the crib sheet, and add to sum
        output_digits = ""
        for value in output_values:
            output_digits += str(crib_sheet[value])
            if crib_sheet[value] in [1, 4, 7, 8]:
                counter += 1

        output_sum += int(output_digits)

    return counter, output_sum


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.read().rstrip().split('\n')
    print(f"1: {solution(input_data)[0]}, 2: {solution(input_data)[1]}")
