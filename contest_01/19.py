def find_repeated_words(text):
    words = text.split()
    word_count = {}
    
    
    for word in words:
        if word == "end":
            break
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    repeated_words = []
    for word, count in word_count.items():
        if count > 1:
            repeated_words.append(word)
    
    
    repeated_words.sort()
    
    return ' '.join(repeated_words)

input_text = input()
result = find_repeated_words(input_text)
print(result)