def count_words(text):
    '''
    Write a new function that accepts the text from the book as a string, 
    and returns the number of words in the string. 
    The .split() method will be helpful here.
    '''
    text_words = text.split()
    number_of_words = len(text_words)
    return number_of_words

def letter_frequency(book):
    '''
    Add a new function to your stats.py file that takes the text from the 
    book as a string, and returns the number of times each character, 
    (including symbols and spaces), appears in the string.

    Convert any character to lowercase using the .lower() method, we don't want duplicates.
    '''
    lower_book = book.lower().replace(' ','')
    letters = []
    for letter in lower_book:
        letters.append(letter)
    unique_letters = set(letters)
    letter_count_dict = {}
    for letter in unique_letters:
        letter_count = lower_book.count(letter)
        # foo = type(letter_count)
        # print(f'letter {letter} appeared {letter_count} many times. Letter count is type {foo}')
        letter_count_dict[letter] = letter_count
        # print(letter_count_dict)
    
    return letter_count_dict

def sorted_dict(dictionary):
    '''
    Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
    Use the .sort() method:
    Use a helper function to return the "num" key of each dictionary for comparison.
    Sort the list from greatest to least by the count.
    '''
    list_of_dicts = []
    for section in dictionary:
        list_of_dicts.append({"letter": section, "num": dictionary[section]})
    
    # The below is a function specifically to be passed to the sort method
    def sort_on(dictionary):
        return dictionary["num"]
    
    # print(list_of_dicts[0]["num"])
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts