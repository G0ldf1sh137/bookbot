def main():
  book_path = './books/frankenstein.txt'
  text = get_book_text(book_path)
  print(text)
  num_words = len(text.split())
  print(f'{num_words} words long!')

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
if __name__ == '__main__':
  main()
