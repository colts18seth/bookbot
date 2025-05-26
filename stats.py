def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_words(sys_argv):
    total = len(get_book_text(str(sys_argv[1])).split())
    return total

def get_chars(sys_argv):
    chars_dict = {}
    for char in get_book_text(str(sys_argv[1])):
        if char.lower() in chars_dict:
            chars_dict[char.lower()] += 1
        else:
            chars_dict[char.lower()] = 1
    return chars_dict

def sorted_list(sys_argv):
    chars_list = []
    chars_dict = get_chars(sys_argv)
    for k,v in chars_dict.items():
        if k.isalpha():
            chars_list.append({"char": k, "num": v})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(dict):
    return dict["num"]