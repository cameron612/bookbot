path = "./books/frankenstein.txt"

def get_num_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def get_num_letters(file_contents):
    char_dict = {}
    word_list = file_contents.split()
    for word in word_list:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

### create a report which returns the alphabetic characters in the text ranked by occurrence
def generate_book_report(file_contents):
    char_dict = {}
    word_list = file_contents.split()
    for word in word_list:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    print(f"--- Begin report of {path} ---")
    print(f"{len(word_list)} words found in document\n")


    def sort_on(dict):
        return dict["count"]
    
    char_dict_list = []
    for dict_entry in char_dict:
        char_dict_list.append({"char":dict_entry, "count":char_dict[dict_entry]})

    char_dict_list.sort(reverse=True, key=sort_on)
    for char_dict in char_dict_list:
        if char_dict["char"] >= 'a' and char_dict["char"] <= 'z':
            print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")
    print("--- End report ---")


def main():
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)
        print(get_num_words(file_contents))
        print(get_num_letters(file_contents))
        generate_book_report(file_contents)

main()