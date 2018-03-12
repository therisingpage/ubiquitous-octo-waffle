import re
from collections import Counter


def count_words(sentence):
    '''
    Solution algorithm provided by Truthful Technologies.

    :param sentence:
    :return: Mappable object with count of words from the param
    '''
    return Counter(re.findall(r"[\w'-]+", sentence.lower()))
