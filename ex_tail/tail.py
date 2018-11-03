def tail(seq, n):
    '''
    a function that takes a sequence (like a list, string, or tuple)
    and a number n and returns the last n elements
    from the given sequence, as a list

    For example:
    >> tail([1, 2, 3, 4, 5], 3)
    [3, 4, 5]
    >> tail('hello', 2)
    ['l', 'o']
    >> tail('hello', 0)
    []


    :param seq:
    :param n:
    :return: list of last n elements
    '''

    if n:
        return seq[-n:]
        # return a list here.

    # return seq[-n:]


print(tail([1, 2, 3, 4, 5], 3))
print(tail('hello', 2))
print(tail('hello', 0))
