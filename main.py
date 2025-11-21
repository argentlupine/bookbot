from stats import count_words, letter_frequency, sorted_dict
import sys

def get_book_text(filepath):
    '''
    It takes a filepath as input and returns the contents of the file as a string.
    '''
    with open(filepath) as f:
        filecontents = f.read()
    
    return filecontents

# book_path = 'books/frankenstein.txt'

def main(book_path):
    book = get_book_text(book_path)
    word_number = count_words(book)
    unique_letters = letter_frequency(book)
    sortedish = sorted_dict(unique_letters)
    print(f'========== BOOKBOT ==========')
    print(f'Analysing book found at {book_path}')
    print(f'--------- Wordcount ---------')
    print(f'Found {word_number} total words')
    print(f'------ Character Count ------')
    for list_item in sortedish:
        print(f'{list_item["letter"]}: {list_item["num"]}')
    print(f'============ END ============')

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        main(book_path=sys.argv[1])