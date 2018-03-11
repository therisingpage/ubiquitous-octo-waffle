def earliest_solution(date_1, date_2):
    '''
        Solution algorithm provided by Truthful Technologies
        It uses tuple unpacking!! This is a lot cleaner than
        my previous solution

        :param date_one: string of first date
        :param date_two: string of second date
        :return: string of the earliest date
        '''

    month_one, day_one, year_one = date_1.split("/")
    month_two, day_two, year_two = date_2.split("/")

    if (year_one, month_one, day_one) < (year_two, month_two, day_two):
        return date_1
    else:
        return date_2
