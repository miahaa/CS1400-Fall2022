# Functions to process audio.
# For CS 1400, written by David E. Johnson.
# Function implementations by Thu Ha
import random

# Add your functions below this line
def make_reversed_samples(list):
    """Return a list in reverse order

    :param list:
    :return: a list in reverse order
    """
    new_list = []
    for i in range(len(list)):
        a = list[len(list)-i-1]
        new_list.append(a)
    return new_list


def make_louder_samples(list, scale_number):
    """ Return a list with every element in the original list multiplied by the scale parameter.

    :param list:
    :param scale_number:
    :return: a list with every element in the original list multiplied by the scale parameter.
    """
    new_list = []
    for i in list:
        multiplied_number = i * scale_number
        new_list.append(multiplied_number)
    return new_list

def make_clipped_samples(list, clip_level_number):
    """Return list made up of every element in the original list with the value of new elements set to be within a certain range

    :param list:
    :param clip_level_number:
    :return: a list made up of every element in the original list with the value of new elements set to be within a certain range
    """
    new_list = []
    for i in list:
        if i > clip_level_number:
            i = clip_level_number
        if i < -clip_level_number:
            i = -clip_level_number
        new_list.append(i)
    return new_list


def make_noisy_samples(list, noise_level_number):
    """Return list made up of every element in the original list with some noise added to each value

    :param list:
    :param noise_level_number:
    :return: a list made up of every element in the original list with some noise added to each value
    """
    new_list = []
    for i in list:
        random_number = random.randrange(-noise_level_number, noise_level_number + 1)
        added_number = i + random_number
        new_list.append(added_number)
    return new_list


def make_smoothed_samples(list):
    """ Return a list with each element is an average of the values around it from the original list

    :param list:
    :return: a list with each element is an average of the values around it from the original list
    """
    new_list = []
    for i in range(len(list)):
        if i == 0:
            average_number = (list[0] + list[1]) // 2
        elif i == len(list)-1:
            average_number = (list[len(list)-1] + list[len(list)-2]) // 2
        else:
            average_number = (list[i + 1] + list[i - 1] + list[i]) // 3
        new_list.append(average_number)
    return new_list







# You can add small test examples here and see results from running this file instead
# of the SoundApp
def main():
    print("Testing the make_reversed_samples function")
    print("Testing make_reversed_samples([5, 4, 3, 2, 1]). Expecting the result of [1, 2, 3, 4, 5] and computed the result of", make_reversed_samples([5, 4, 3, 2, 1]))
    print()

    print("Testing the make_louder_samples function")
    print("Testing make_louder_samples([2, 4, 6], 10). Expecting the result of [20, 40, 60] and computed the result of", make_louder_samples([2, 4, 6], 10))
    print()

    print("Testing the make_clipped_samples function")
    print("Testing make_clipped_samples([-5, -1, 2, 5, 10], 4). Expecting the result of [-4, -1, 2, 4, 4] and computed the result of", make_clipped_samples([-5, -1, 2, 5, 10], 4))
    print()

    print("Testing the make_noisy_samples function")
    print("Testing make_noisy_samples([10, 20, 30], 3) and computed the result of", make_noisy_samples([10, 20, 30], 3))
    print()

    print("Testing the make_smoothed_samples function")
    print("Testing make_smoothed_samples([0, 100, 500, -100]). Expecting the result of [50, 200, 166, 200] and computed the result of", make_smoothed_samples([0, 100, 500, -100]))


if __name__ == "__main__":
    main()