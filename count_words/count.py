def count_words(sentence):
    '''
    Python Morsels Exercise 2: Count the number of times a word
    appears in a sentence

    :param sentence: A string of words
    :return: mapable like structure with counts of words
    '''
    result = {}
    sentence = sentence.lower()

    for x in sentence.split():
        if x in result:
            result[x] = result[x] + 1
        else:
            result[x] = 1

    return result


# Test Cases
print(count_words("oh what a day what a lovely day"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

print(count_words("don't stop believing"))
# {"don't": 1, 'stop': 1, 'believing': 1}

print(count_words("Oh what a day what a lovely day"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

print(count_words("Oh what a day, what a lovely day!"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
