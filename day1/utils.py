def pass_from_zero(actual_number, direction, moves):
    """Counts how many times we pass from zero."""
    result = 0
    i = actual_number

    if direction == "R":
        while moves > 0:
            moves -= 1
            i += 1
            if i == 100:
                i = 0
                result += 1
    elif direction == "L":
        while moves > 0:
            moves -= 1
            i -= 1
            if i == 0:
                result += 1
            if i == -1:
                i = 99

    return result
