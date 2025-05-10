from stats import get_number_of_words, get_frequency
import sys
def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]
    num_of_words=get_number_of_words(path)
    char_frequency=get_frequency(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for key,value in char_frequency.items():
        if key == '\n':
            print(f"\\n: {value}")
        else:
            print(f"{key}: {value}")
    print("============= END ===============")



main()