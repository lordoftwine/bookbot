from stats import get_num_words, get_book_text, count_characters, sort_output, format_char_dictionary
import sys


def main(bookpath):
    path = bookpath
    text = get_book_text(path)
    num_of_words = get_num_words(text)
    char_count = count_characters(text)
    sorted_dictionary = sort_output(char_count)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    format_char_dictionary(sorted_dictionary)
    print("============= END ===============")
    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])