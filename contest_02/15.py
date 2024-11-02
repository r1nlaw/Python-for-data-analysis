def leg_count_in_longest_sequence(legs):
    if not legs:
        return 0

    max_length = 1
    current_length = 1
    max_leg = legs[0]

    for i in range(1, len(legs)):
        if legs[i] == legs[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_leg = legs[i]
        else:
            current_length = 1

    return max_leg
