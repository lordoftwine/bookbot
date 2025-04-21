from stats import get_num_words, get_book_text, count_characters

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_of_words = get_num_words(text)
    char_count = count_characters(text)

    print(f"{num_of_words} words found in the document")
    print(char_count)

main()