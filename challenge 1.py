import math


def solution(i):
    """ A function which takes an integer between 0 and 10000 as input,
    uses it as the index number passed into a single string of all ordered prime numbers,
    and returns a 5-digit ID number of the next 5 digits in the string starting at the specified index. """

    # function for checking the total concatenated character length of all values in a list given the addition of a new value
    length_list = []

    def get_total_length(x):
        length_list.append(len(str(x)))
        return sum(length_list)

    # creates a list of all prime numbers in order, up to a total concatenated character length of 10005
    # (prompt: # minions up to 10000 = starting index up to 10000, whose 5 digit ID would extend to index 10004)
    list_of_primes = [n for n in range(2, 100000) if all(n % m != 0 for m in range(2, int(math.sqrt(n)) + 1))
                      if get_total_length(n) < 10005]

    # creates a single string of concatenated prime numbers
    string_of_primes = "".join(map(str, list_of_primes))

    # selects and return 5 digit ID based on the input
    minion_id = string_of_primes[i:i+5]
    return minion_id


print(solution(3))