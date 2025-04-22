def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def get_num_words(text):
    num_of_words = len(text.split())
    #print(f"{num_of_words} words found in the document")
    return (num_of_words)

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return(char_count)

def sort_output(input_dictionary):
    dictionary_as_list = list(input_dictionary.items())
    sorted_dictionary = sorted(dictionary_as_list, key=lambda item: item[1], reverse=True)
    return sorted_dictionary

def format_char_dictionary(sorted_list):
    for char, count in sorted_list:
        if char.isalpha():
            print(f"{char}: {count}")