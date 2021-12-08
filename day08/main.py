"""
--- Day 8: Seven Segment Search ---
"""


def inner_pattern(list1, list2) -> bool:
    """
    Returns True if all elements of list1 exist in list2, False otherwise
    """
    for el in list1:
        if el not in list2:
            return False

    return True


def solution(signal_notes: list) -> tuple:
    """
    returns tuple (part1, part2)
    there's also got to be a nicer way...
    """

    counter = 0
    output_sum = 0
    for note in signal_notes:
        signal_patterns, output_value = note.split(
            " | ")[0], note.split(" | ")[1]

        crib_sheet = {0: "", 1: "", 2: "", 3: "", 4: "",
                      5: "", 6: "", 7: "", 8: "", 9: ""}

        signal_patterns = signal_patterns.split(" ")
        unknown_signal_patterns = signal_patterns.copy()

        for signal in signal_patterns:
            if len(signal) in [2, 3, 4, 7]:
                match len(signal):
                    case 2:
                        crib_sheet[1] = signal
                        unknown_signal_patterns.remove(signal)

                    case 3:
                        crib_sheet[7] = signal
                        unknown_signal_patterns.remove(signal)

                    case 4:
                        crib_sheet[4] = signal
                        unknown_signal_patterns.remove(signal)

                    case 7:
                        crib_sheet[8] = signal
                        unknown_signal_patterns.remove(signal)

        for signal in unknown_signal_patterns:

            # All remaining signals are 2,3,5 or 0,6,9
            if len(signal) == 5:
                # Signal is 2,3 or 5
                if inner_pattern(crib_sheet[7], signal):
                    crib_sheet[3] = signal
                else:
                    # 2 or 5
                    if len(list(set(crib_sheet[4]).intersection(signal))) == 3:
                        crib_sheet[5] = signal
                    else:
                        crib_sheet[2] = signal
            elif len(signal) == 6:
                # Signal is 0, 6 or 9
                if inner_pattern(crib_sheet[4], signal):
                    crib_sheet[9] = signal
                else:
                    # 0 or 6
                    if inner_pattern(crib_sheet[7], signal):
                        crib_sheet[0] = signal
                    else:
                        crib_sheet[6] = signal
            else:
                return 0, 0

        # Reverse the crib_sheet to pattern: digit, and sort the patterns for easier matching
        crib_sheet = {"".join(sorted(v)): k for k, v in crib_sheet.items()}

        # Now, go through the output, lookup the combinations in the crib sheet, and add to sum
        output_digits = ""
        for value in output_value.split(" "):
            crib = "".join(sorted(value))
            output_digits += str(crib_sheet[crib])
            if crib_sheet[crib] in [1, 4, 7, 8]:
                counter += 1

        output_sum += int(output_digits)

    return counter, output_sum


if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as file:
        input_data = file.read().rstrip().split('\n')
    print(f"1: {solution(input_data)[0]}, 2: {solution(input_data)[1]}")
