# We are missing one test case here -
# We need to return an iterator object


def compact(seq_char):
    '''
    For this week's exercise
    I want you to write a function that accepts a sequence
    (a list for example) and returns a new iterable
    (anything you can loop over) with adjacent duplicate
    values removed.

    compact([1, 1, 1])
    [1]
    compact([1, 1, 2, 2, 3, 2])
    [1, 2, 3, 2]
    compact([])
    []


    :param seq_char:
    :return: returns iterable with adjacent values removed
    '''

    result = []

    for index, l in enumerate(seq_char):
        # check if list is empty

        if not result:
            result.append(l)
        else:
            # Check the adjacent element:
            # check the size of the result list
            # and then return the last element

            len_result = len(result)
            prev_element_index = len_result - 1
            prev_element = result[prev_element_index]

            if l != prev_element:
                result.append(l)

    return [n for n in result]


# Testing with example cases
x = compact([1, 1, 1])
y = compact([1, 1, 2, 2, 3, 2])
z = [ ]
print(x)
print(y)
print(z)

# nums = (n**2 for n in [1, 2, 3])
# y = compact(nums)
# print(y)
