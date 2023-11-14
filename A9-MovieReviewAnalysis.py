"""
Initial code by David Johnson. This code and derived works may not be posted publicly.

Code finished by Thu Ha.
"""

# Add your critical thinking sentences and example review as described in the assignment here.
"""
The prediction from compare_prediction_with_actual function is not really accurate. It does not have 
enough data to calculate an accurate result. The result's uncertainty is around +-1. For example, the 
actual review is: 'this politic movie is so subjective and cringe' and the function computed the result of 3.42
"""

# Add your functions here.
def make_lowercase_lines_from_file(file_name):
    """
    Return a list where each item in the list is a line from the file. Call the string lower() method on each line to make it lowercase letters.
    :param file_name: A string with a filename in it
    :return: a list where each item in the list is a line from the file. Call the string lower() method on each line to make it lowercase letters.
    """
    # open file
    open_file = open(file_name, encoding="utf-8")
    file_lines = open_file.readlines()
    new_lower_file_lines = []
    # loop each line from file
    for line in file_lines:
        line = line.strip("\n")
        line = line.strip(" \t")
        lower_line = line.lower()
        new_lower_file_lines.append(lower_line)
    return new_lower_file_lines


def make_word_total_value_dict_from_lines(lowercase_string_list):
    """
    Return a dict with every word from the list as keys and the total value of the word as the value
    :param lowercase_string_list: A list of lowercase string values, each string must start with a number and then have words following.
    :return: a dict with every word from the list as keys and the total value of the word as the value
    """
    word_total_dictionary = {}
    # split the string
    for string in lowercase_string_list:
        words = string.split(' ')
        score = int(words[0])
        for word in words[1:]:
            if word in word_total_dictionary:
                word_total_dictionary[word] = word_total_dictionary[word] + score
            else:
                word_total_dictionary[word] = score
    return word_total_dictionary


def make_word_total_count_dict_from_lines(lowercase_string_list):
    """
    Return a dict with every word from the list as keys and the total number of times it appears in all the reviews as the value
    :param lowercase_string_list: a list of lowercase string values. Each string must start with a number and then have words following.
    :return: a dict with every word from the list as keys and the total number of times it appears in all the reviews as the value
    """
    word_count_dictionary = {}
    for string in lowercase_string_list:
        words = string.split(' ')
        for word in words[1:]:
            if word in word_count_dictionary:
                word_count_dictionary[word] = word_count_dictionary[word] + 1
            else:
                word_count_dictionary[word] = 1
    return word_count_dictionary


def make_word_avg_value_from_total_and_count(word_total_dict, word_count_dict):
    """
    Return a dict with every word from the parameter dicts and the average of the total value and count for the word as the value in this new dict
    :param word_total_dict: The word_total_dict
    :param word_count_dict: The word_count_dict
    :return: a dict with every word from the parameter dicts and the average of the total value and count for the word as the value in this new dict
    """
    avg_value_dictionary = {}
    for word in word_total_dict:
        word_avg_value = word_total_dict.get(word) / word_count_dict.get(word)
        if word_avg_value < 1.75 or word_avg_value > 2.25:
            avg_value_dictionary[word] = word_avg_value
    return avg_value_dictionary


def predict_review(review_string, avg_value_dict):
    """
    Return a number score predicting a movie rating for the string
    :param review_string: A string with the words from a review
    :param avg_value_dict: the average_value dict with words and their value
    :return: a number score predicting a movie rating for the string
    """
    word_list = review_string.split(' ')
    total_score = 0
    word_count = 0
    for word in word_list:
        if word in avg_value_dict:
            word_count += 1
            total_score += avg_value_dict[word]
        else:
            pass
    if word_count != 0:
        predict_score = total_score / word_count
    else:
        predict_score = -1
    return predict_score



def compare_prediction_with_actual(lines, avg_value_dict):
    """
    Given a list of movie reviews and a dictionary of words and their average value, compare
    the predicted rating with the actual rating.
    :param lines: a list of movie reviews. Each review starts with a 0 to 4 movie rating.
    :param avg_value_dict: A dict of words and their average value in a movie review rating
    :return: None. This prints out some predicted and actual score for movie reviews.
    """
    for line in lines:
        words = line.split()
        actual_score = int(words[0])
        predicted_score = predict_review(" ".join(words[1:]), avg_value_dict)
        print("predicted:", predicted_score, "actual:", line)

def main():
    """
    Read a file of movie reviews, develop a dictionary of word values, and use
    those to make movie rating predictions.
    """
    # Add some testing code below here. Make a small list of reviews by hand or read in a small
    # file. Make small total value and count dictionaries to test the average function. Make a small
    # average dictionary to test the prediction function. Make these by hand to make the tests be as independent
    # from each other as possible.

    print("Testing the make_word_total_value_dict_from_lines function")
    print("Testing make_word_total_value_dict_from_lines(['3 a good movie', '2 a pretty bad movie']). "
          "Expecting the result of {'a': 5, 'good': 3, 'movie': 5, 'pretty': 2, 'bad': 2} "
          "and computed the result of", make_word_total_value_dict_from_lines(['3 a good movie', '2 a pretty bad movie']))
    print()

    print("Testing the make_word_total_count_dict_from_lines function")
    print("Testing make_word_total_count_dict_from_lines(['3 a good movie', '2 a pretty bad movie']). "                   
           "Expecting the result of {'a': 2, 'good': 1, 'movie': 2, 'pretty': 1, 'bad': 1}"                               
           " and computed the result of", make_word_total_count_dict_from_lines(['3 a good movie', '2 a pretty bad movie']))
    print()

    print("Testing the make_word_avg_value_from_total_and_count function")
    print("Testing make_word_avg_value_from_total_and_count([{'a': 5, 'good': 3, 'movie': 5, 'pretty': 2, 'bad': 2}, "
          "{'a': 2, 'good': 1, 'movie': 2, 'pretty': 1, 'bad': 1}]). "                    
           "Expecting the result of and computed the result of {'a': 2.5, 'good': 3.0, 'movie': 2.5}",
          make_word_avg_value_from_total_and_count({'a': 5, 'good': 3, 'movie': 5, 'pretty': 2, 'bad': 2},
                                                   {'a': 2, 'good': 1, 'movie': 2, 'pretty': 1, 'bad': 1}))
    print()

    print("Testing the predict_review function")
    print("Testing predict_review('A magically interesting movie', {'a': 2.5, 'good': 3.0, 'movie': 2.5}). Expecting the result of 2.5 and computed the result of", predict_review("A magically interesting movie", {'a': 2.5, 'good': 3.0, 'movie': 2.5}))
    print()



    # You should not need to change the code below here. You can comment out some of the print statements if
    # they are producing so much text it is confusing.

    # read the reviews into a list
    lines = make_lowercase_lines_from_file("smallReviews.txt")
    # lines = make_lowercase_lines_from_file("MovieReviews.txt") # uncomment this when you are ready to try the full set of reviews.
    print(lines) # examine the result

    # Make a dict with words from reviews and their summed up values from the reviews they are in
    total_value_dict = make_word_total_value_dict_from_lines(lines)
    print(total_value_dict) # examine the dict to see if it looks correct

    # Count up how often a word appears in all the reviews
    total_count_dict = make_word_total_count_dict_from_lines(lines)
    print(total_count_dict) # examine the dict to see if it looks correct

    # Get the average value per word from the total value and their count
    avg_value_dict = make_word_avg_value_from_total_and_count(total_value_dict, total_count_dict)
    print(avg_value_dict) # examine the dict to see if it looks correct

    # Compare actual and predicted movie ratings for a small number of reviews
    if len(lines) < 110:
        compare_prediction_with_actual(lines, avg_value_dict) # use all for small review files
    else:
        compare_prediction_with_actual(lines[100:110], avg_value_dict)

    # Ask the user for a movie review and predict a rating. It should be without punctuation.
    personal_movie_review = input("Please enter a review with no punctuation: ")
    personal_movie_review = personal_movie_review.lower()
    prediction = predict_review(personal_movie_review, avg_value_dict)
    print("The predicted review score is", prediction)

if __name__=="__main__":
    main()