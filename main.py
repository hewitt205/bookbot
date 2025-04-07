import sys
from stats import count_words, count_characters, sorted_characters

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        text = get_book_text(path_to_file)
        total_words = count_words(text)
        chars = count_characters(text)
        sorted_list = sorted_characters(chars)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")

        for dict in sorted_list:
            character = dict['character']
            if character.isalpha():
                print(f"{character}: {dict['num']}")
        print("============= END ===============")

main()
