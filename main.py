def main():
  book_path = './books/frankenstein.txt'
  text = get_book_text(book_path)
  print(f"--- begin book report of {book_path} ---")
  
  num_words = get_word_count(text)
  print(f'{num_words} words long!')

  char_dict = get_char_dict(text)
  sorted = char_dict_to_sorted_list(char_dict)
  print("SORTED", sorted)
  for item in sorted:
    if not item["char"].isalpha():
      continue
    print(f"The '{item['char']}' character was found {item['count']} times")
  print(" --- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_word_count(text):
  return len(text.split())

def get_char_dict(text):
  output = dict()
  lowered = text.lower()
  for char in lowered:
    if char not in output:
      output[char] = 1
    else:
      output[char] += 1
  return output

def sort_on(dict):
    return dict["count"]

def char_dict_to_sorted_list(char_dict):
  sorted = []
  for char in char_dict:
    sorted.append({"char": char, "count": char_dict[char]})
  sorted.sort(reverse=True, key=sort_on)
  return sorted
  
if __name__ == '__main__':
  main()
