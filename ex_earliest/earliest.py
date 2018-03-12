
def get_earliest(date_one, date_two):
    '''
    This function will compare two dates
    and return the ex_earliest date of the two

    Normally, we should be able to use datetime, however,
    we want to include weird dates too, the function should also be able to take in
    wrong dates and compare them: 02/40/2006 is before 03/01/2006 but after 02/30/2006
    (dates don't rollover at all)

    ** This algorithm uses splitting and indexing, which might get dicey
    ** As per the solution from TruthTech (which i didn't look at until the end :) ),
    It is more pythonic to use tuple-unpacking.

    :param date_one: string of first date
    :param date_two: string of second date
    :return: string of the earliest date
    '''

    # split the string returned using "/"
    elements_one = date_one.split("/")
    elements_two = date_two.split("/")

    # Parse the years
    if int(elements_one[2]) == int(elements_two[2]):

        # Parse the months
        if int(elements_one[0]) == int(elements_two[0]):

            # Parse the days
            if int(elements_one[1]) == int(elements_two[1]):
                earliest = date_one
            elif int(elements_one[1]) > int(elements_two[1]):
                earliest = date_two
            else:
                earliest = date_one

        elif int(elements_one[0]) > int(elements_two[0]):
            earliest = date_two
        else:
            earliest = date_one

    elif int(elements_one[2]) > int(elements_two[2]):
        earliest = date_two
    else:
        earliest = date_one

    return earliest


# Test Cases
a = get_earliest("01/27/1756", "01/28/1756")
print(a)

a = get_earliest("01/27/1832", "01/27/1756")
print(a)

b = get_earliest("02/29/1972", "12/21/1946")
print(b)
# "12/21/1946"

c = get_earliest("02/24/1946", "03/21/1946")
print(c)
# "02/24/1946"

d = get_earliest("06/21/1958", "06/24/1958")
print(d)
# "06/21/1958"

e = get_earliest("03/01/2006", "02/40/2006")
print(e)

r = get_earliest("02/40/2006", "02/30/2006")
print(r)
