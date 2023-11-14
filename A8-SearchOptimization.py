"""
    A8 starter code written by David Johnson. All derived works must not
    be posted publicly.

    A8 assignment completed by Thu Ha
"""


# Fill in the required assignment functions below here.
def curve_scores(list):
    """
    Return a new list of numbers changed so that the highest number in the parameter list becomes 100 and all the other numbers are moved up by the same amount.
    :param list: containing integer numbers that can range from 0 to 100
    :return: a list of numbers changed so that the highest number in the parameter list becomes 100 and all the other numbers are moved up by the same amount.
    """
    if list == []:
        return []
    max_value = list[0]
    for number in list:
        if max_value < number:
            max_value = number
    difference = 100 - max_value
    new_list = []
    for i in list:
        a = i + difference
        new_list.append(a)
    return new_list


def contains_duplicate(list):
    """
    Return True if the list contains the same string twice or more, otherwise False
    :param list: A list of string values.
    :return: True if the list contains the same string twice or more, otherwise False
    """
    if list == []:
        return False
    for index in range(len(list) - 1):
        if list[index] in list[index + 1: len(list)]:
            return True
    return False


def list_to_string(list):
    """
    Return A string containing a text representation of the list
    :param list: A list of integer values.
    :return: A string containing a text representation of the list
    """
    if list == []:
        return "[]"
    string = "["
    for index in range(len(list)):
        if index == len(list) - 1:
            string = string + str(list[index]) + "]"
        else:
            string = string + str(list[index]) + ', '
    return string


def find_smallest_positive_number(list):
    """
    Return an integer value that is the smallest number greater than 0 in the list or None if there are no positive numbers in the list.
    :param list: A list of integer values.
    :return: an integer value that is the smallest number greater than 0 in the list or None if there are no positive numbers in the list.
    """
    new_list = []
    for number in list:
        if number > 0:
            new_list.append(number)
    if new_list == []:
        return None
    smallest_number = new_list[0]
    for number in new_list:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

def lines_from_file(filename):
    """
     Return a new list of string values, where each value is a line from the file.
    :param filename: a string holding the name of the file to read the lines from.
    :return: a new list of string values, where each value is a line from the file.
    """
    open_file = open(filename, encoding="utf-8")
    file_lines = open_file.readlines()
    return file_lines



def binary_search_for_matching_string(key, values):
    """
    Return the location of key in the values list, or None if no match. This function uses
    binary search to efficiently search a sorted list.

    :param key: The item to search for
    :param values: A sorted list of values
    :return: The location of the matching item or None if no match.
    """
    lo = 0
    hi = len(values) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if values[mid].startswith(key):  # if key found return where it is
            return values[mid]
        elif values[mid] < key: # If the checked value is less than key, remove left half of list
            lo = mid + 1
        else:                   # If the checked value is greater than key, remove right half of list
            hi = mid - 1
    return None


def main():
    print("Testing the curve_scores function")
    print("Testing curve_score([45, 85, 90]). Expecting the result of [55, 95, 100] and computed the result of", curve_scores([45, 85, 90]))
    print()
    print("Testing the contains_duplicate function")
    print("Testing contains_duplicate(['hi', 'bye']). Expecting the result of False and computed the result of", contains_duplicate(["hi", "bye"]))
    print("Testing contains_duplicate(['the', 'boy', 'the']). Expecting the result of True and computed the result of", contains_duplicate(["the", "boy", "the"]))
    print()
    print("Testing the list_to_string function")
    print("Testing list_to_string([1, 2, 3]). Expecting the result of [1, 2, 3] and computed the result of", list_to_string([1, 2, 3]))
    print()
    print("Testing the find_smallest_positive_number function")
    print("Testing find_smallest_positive_number([2, -4, 5]). Expecting the result of 2 and computed the result of", find_smallest_positive_number([2,  -4,  5]))
    print()
    print("Testing the binary_search_for_matching_string function")
    print("Testing binary_search_for_matching_string('ca', ['apple', 'cat', 'dog']). Expecting the result of cat and computed the result of", binary_search_for_matching_string("ca", ["apple", "cat", "dog"]))

if __name__ == "__main__":
    main()