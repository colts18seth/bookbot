import sys
from stats import get_words, sorted_list

def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_words(sys.argv)} total words")
        print("--------- Character Count -------")
        chars_list = sorted_list(sys.argv)
        for char in chars_list:
            print(f'{char["char"]}: {char["num"]}')
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()