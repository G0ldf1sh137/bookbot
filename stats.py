def get_word_count(text):
    num_words = len(text.split())
    return num_words




def get_char_count(text):
    result = dict()
    
    for char in text.lower():
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    
    return result


def sort_on(d):
    return d['num']



def get_sorted_chars(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list