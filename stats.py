def count_words(path_to_file):
    words = len(path_to_file.split())
    return words

def counter(text):
    dict = {}
    text = text.lower()
    for t in text:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    return dict
 
def sort_char_count(char_counts):
    result = []
    for char, count in char_counts.items():
        result.append({"char": char, "count": count})
    result.sort(reverse=True, key=lambda x: x["count"])
    return result
