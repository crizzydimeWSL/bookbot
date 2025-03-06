def count_words(text):
    words = text.split()
    return len(words)


def count_char(text):

    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_char_counts(char_count):

    filtered_counts = {char: count for char, count in char_count.items() if char.isalpha()}
    sorted_list = sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True)

    return [{"character": char, "count": count} for char, count in sorted_list]



    

    


