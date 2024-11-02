import math
from collections import Counter

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def get_frequency_dict(text):
    return Counter(text)

def normalize_dicts(dict1, dict2):
    all_keys = set(dict1.keys()).union(set(dict2.keys()))
    for key in all_keys:
        if key not in dict1:
            dict1[key] = 0
        if key not in dict2:
            dict2[key] = 0
    return dict1, dict2

def cosine_similarity(dict1, dict2):
    dict1, dict2 = normalize_dicts(dict1, dict2)
    
    dot_product = sum(dict1[key] * dict2[key] for key in dict1)
    norm1 = math.sqrt(sum(dict1[key] ** 2 for key in dict1))
    norm2 = math.sqrt(sum(dict2[key] ** 2 for key in dict2))
    
    if norm1 == 0 or norm2 == 0:
        return 0
    
    return dot_product / (norm1 * norm2)

def determine_language(input_text, en_text, rus_text):
    input_freq = get_frequency_dict(input_text)
    en_freq = get_frequency_dict(en_text)
    rus_freq = get_frequency_dict(rus_text)
    
    input_en_similarity = cosine_similarity(input_freq, en_freq)
    input_rus_similarity = cosine_similarity(input_freq, rus_freq)
    
    if input_en_similarity > input_rus_similarity:
        return "EN"
    else:
        return "RUS"

def main():
    en_text = read_file('trainEN.txt')
    rus_text = read_file('trainRUS.txt')
    input_text = read_file('input.txt')
    
    result = determine_language(input_text, en_text, rus_text)
    print(result)

if __name__ == "__main__":
    main()