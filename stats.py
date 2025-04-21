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
