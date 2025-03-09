from collections import defaultdict


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = defaultdict(int)
    for char in text.lower():
        characters[char] += 1
    return dict(characters)

def sorted_report(characters):
    sorted_list = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    filtered_list = []
    for char, count in sorted_list:
        if char.isalpha():
            filtered_list.append((char, count))
    return filtered_list




