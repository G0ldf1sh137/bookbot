import sys

from stats import get_word_count, get_char_count, get_sorted_chars

def main():
    
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    source = sys.argv[1]
    text = get_book_text(source)
    word_count = get_word_count(text)
    chars = get_char_count(text)
    sorted_chars = get_sorted_chars(chars)
    
    print_report(source, word_count, sorted_chars)
    
    
    



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
    
    
    
def print_report(source, num_words, sorted_chars):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {source}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for record in sorted_chars:
        if record['char'].isalpha():
            print(f"{record['char']}: {record['num']}")
    print('============= END ===============')


if __name__ == "__main__":
    main()