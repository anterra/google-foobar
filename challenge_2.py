# a function to convert an integer into a number of any base n
def int_to_base_n(number, base):
    str_base_n = ""
    while number:
        mod = number % base
        number = number // base
        str_base_n = str(mod) + str_base_n
    return str_base_n


list_of_results = []


def solution(n, b):
    """ Accepts a string number as 'n' and an int 'b' as the base of that number,
    creates variables based off input and performs operations on them until results
    are infinitely repeating values, returns how many unique repeating values there are. """

    while True:
        # defines variables (x is digits of n in descending order, y is digits of n in ascending),
        # converting string input in base b into equivalent int value
        x_str = "".join(reversed(sorted(n)))
        x = int(x_str, b)
        y_str = "".join(sorted(n))
        y = int(y_str, b)

        # performs operations on variables in int form, converts result back to base b string form
        z_int = x - y
        z = int_to_base_n(z_int, b)
        z_str = str(z)

        # adds leading zeros to string form if result is less than original length
        k = len(n)
        if len(z_str) != k:
            right_length_z = z_str.zfill(k)
            z = right_length_z
        else:
            z = z_str

        # reassigns result as input, to loop
        n = z

        # adds each result to a list, finds those which are infinitely repeating (greater than 10 repetitions chosen
        # as sufficiently repeating) and returns how many unique repeating values there are
        list_of_results.append(z)
        list_of_duplicates = [x for x in list_of_results if list_of_results.count(x) > 10]
        unique_duplicates = set(list_of_duplicates)
        result = len(unique_duplicates)

        # breaks the loop once it has run a sufficient number of trials
        if len(list_of_results) == 300:
            break
    return result


print(solution("1211", 3))
