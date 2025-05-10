def get_book_text(path):
    with open(path) as f:
        file_contents=f.read()
        return file_contents

def get_number_of_words(path):
    file_contents=get_book_text(path)
    split_words=file_contents.split()
    return len(split_words)

def get_frequency(path):
    file_contents=get_book_text(path)
    file_contents=file_contents.lower()
    char_frequency={}
    for ch in file_contents:
        if ch in char_frequency:
            char_frequency[ch]+=1
        else:
            char_frequency[ch]=1
    return char_frequency
    