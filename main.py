import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sorted_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
     
def main():
    if len(sys.argv) >= 2:    
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        word_count = get_num_words(text)
        character_count = get_num_characters(text)
        report = sorted_report(character_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")

        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")

        print("--------- Character Count -------")
        for char, count in report:
            print(f"{char}: {count}")

        print("============= END ===============")
    else :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
