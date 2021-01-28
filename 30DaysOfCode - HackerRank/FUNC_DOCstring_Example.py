def sum_eo(n, t):
    """Written code in section 6 on udemy by Tume who is one of the students in Udemy online courses

    Args:
        n: integer toon turul
        t: character turul

    Returns:
        a sum of even numbers up to n, if not, then return -1: SMALL PROGRAM
    """
    if t == "e":
        return sum(range(0, n, 2))
    elif t == "o":
        return sum(range(1, n, 2))
    return -1


print(sum_eo(int(input()), input()))