def main():
    path = "books/frankenstein.txt"
    text_content = get_text(path)
    num_words = num_of_words(text_content)
    character_counts = count_characters(text_content)
    sorted_char_dict = dict_to_list(character_counts)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document \n")

    for item in sorted_char_dict:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def num_of_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def dict_to_list(d):
    sorted_characters = []
    for char, count in d.items():
        if not char.isalpha():
            continue
        sorted_characters.append({"char": char, "num": count})
    sorted_characters.sort(reverse=True, key=sort_on)      
    return sorted_characters   

def count_characters(text):
    character_frequencies = {}
    chars = text.lower()
    for char in chars:
        if char in character_frequencies:
            character_frequencies[char] += 1
        else:
            character_frequencies[char] = 1    
    return character_frequencies
    
def get_text(path):
    with open(path) as file_handler:
        return file_handler.read()

main()