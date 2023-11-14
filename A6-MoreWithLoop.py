# Assignment A6
# CS 1400
# Starter code by David Johnson

# Assignment completed by Thu Ha

# The multiply function computes the product of two factors
def multiply(factor1, factor2):
    product = 0
    for loop_counter in range(factor2):
        product += factor1
    return product

# the choose_smaller function returns the smaller of the two parameters
def choose_smaller(number_1, number_2):
    if number_1 < number_2:
        return number_1
    return number_2

# the describe_function shows the number given is positive, negative or equal to 0.
def describe_number(number):
    if number == 0:
        return "zero"
    elif number > 0:
        return "positive"
    elif number < 0:
        return "negative"

# the add_a_or_an_to word funtions adds "a" or "and" before the word given
def add_a_or_an_to_word(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] =="u":
        return "an " + word
    else:
        return "a " + word

# the add_a_or_an_orr_any_to_word funcion add "a" or "an" to the singular word and add "any" to plural word
def add_a_or_an_or_any_to_word(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        return "an " + word
    elif word[-1] == "s":
        return "any " + word
    else:
        return "a " + word

# the pirate_function takes in a sentence in normal English and replace some words with their pirate speech equivalent and return the translated sentence
def pirate_translate(sentence):
    list_of_word = sentence.split()
    for i in range(len(list_of_word)):
        if list_of_word[i] == 'my':
            list_of_word[i] = 'me'
        elif list_of_word[i] == 'you':
            list_of_word[i] = 'ye'
        elif list_of_word[i] == 'is' or list_of_word[i] == 'are':
            list_of_word[i] = 'be'
        elif list_of_word[i] == 'hello':
            list_of_word[i] = 'ahoy'
        elif list_of_word[i] == 'friend':
            list_of_word[i] = 'matey'
        translation = " ".join(list_of_word)
    return translation



# Main tests all the functions and reports on their results
def main():
    print("Testing the multiply function")
    print("Testing multiply(2,3). Expecting a result of 6 and computed a result of", multiply(2,3))
    print("Testing multiply(5,6). Expecting a result of 30 and computed a result of", multiply(5,6))
    print()
    print("Testing the choose smaller function")
    print("Testing choose_smaller(10,11). Expecting a result of 10 and computed a result of", choose_smaller(10,11))
    print("Testing choose_smaller(21,11). Expecting a result of 11 and computed a result of", choose_smaller(21,11))
    print("Testing choose_smaller(30,30). Expecting a result of 30 and computed a result of", choose_smaller(30,30))
    print()
    print("Testing the describe_number function")
    print("Testing describe_number(0). Expecting a result of 'zero' and computed a result of", describe_number(0))
    print("Testing describe_number(-2). Expecting a result of 'negative' and computed a result of", describe_number(-2))
    print("Testing describe_number(5). Expecting a result of 'positive' and computed a result of", describe_number(5))
    print()
    print("Testing add_a_or_an_to_word function")
    print("Testing add_a_or_an_to_word(umbrella). Expecting a result of 'an umbrella' and computed a result of", add_a_or_an_to_word("umbrella"))
    print("Testing add_a_or_an_to_word(car). Expecting a result of 'a car' and computed a result of", add_a_or_an_to_word("car"))
    print()
    print("Testing add_a_or_an_or_any_to_word function")
    print("Testing add_a_or_an_or_any_to_word(apple). Expecting a result of 'an apple' and computed a result of", add_a_or_an_or_any_to_word("apple"))
    print("Testing add_a_or_an_or_any_to_word(cup). Expecting a result of 'a cup' and computed a result of", add_a_or_an_or_any_to_word("cup"))
    print("Testing add_a_or_an_or_any_to_word(bears). Expecting a result of 'any bears' and computed a result of", add_a_or_an_or_any_to_word("bears"))
    print()
    print("Testing pirate_translation function")
    print("Testing pirate_translation(This is my friend). Expecting a result of 'This be me matey' and computed a result of", pirate_translate("This is my friend"))
    print("Testing pirate_translation(hello there are my dogs). Expecting a result of 'Ahoy there be me dogs' and computed a result of", pirate_translate("hello there are my dogs"))
    print("Testing pirate translation(you are a computer scientist). Expecting a result of 'ye be a computer scientist' and computed a result of", pirate_translate("you are a computer scientist"))




if __name__=="__main__":
    main()