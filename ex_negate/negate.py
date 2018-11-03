def negate(nested_list):
    '''
    a function that accepts a list of lists of numbers
    and returns a new list of lists with each
    of the numbers negated.

    It should work something like this:
    >> matrix = [[1, -2], [-3, 4]]
    >> negate(matrix)
    [[-1, 2], [3, -4]]

    >> matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    >> negate(matrix)
    [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]

    :param nested_list:
    :return: negated list of lists

    '''

    result = []
    for x in nested_list:
        nested_result = []
        for i in x:
            nested_result.append(i*-1)
        result.append(nested_result)
    return result

    # This would be more idiomatic
    # but I cannot figure out how to multiply inside a nested list
    # and return a nested list
    # return [x for x in nested_list]


# matrix = [[1, -2], [-3, 4]]
# x = negate(matrix)

matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
x = negate(matrix)
# [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]

print(x)

