from stats import (get_chars_dict, get_num_words, chars_dict_to_sorted_list)
import sys

def get_book_text(path_to_file: str):
    file_contents = str("")
    with open(path_to_file) as f:
        file_contents = str(f.read())
        
    return file_contents

def main():

    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print_report(book_path, num_words, chars_sorted_list)
    else:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()