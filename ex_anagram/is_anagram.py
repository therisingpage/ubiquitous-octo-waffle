def is_anagram(first, second):
    '''
    Write a function that accepts two strings and returns True
    if the two strings are anagrams of each other.

    :return: Boolean
    '''

    # convert to lower case
    x = first.lower()
    y = second.lower()

    # arrange the letters in both words
    return sorted(x) == sorted(y)

print(is_anagram("tea", "eat"))
# True
print(is_anagram("tea", "treat"))
# False
print(is_anagram("sinks", "skin"))
# False
print(is_anagram("Listen", "silent"))
# True