def count_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words += 1
    #print (f"{num_words} words found in the document")
    return num_words

def count_characters(book_text):
    character_counts = {}
    for character in book_text.lower():
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def sort_on(dictionary):
    return dictionary["num"]

def sorted_characters(character_dictionary):
    character_sort = []
    for key in character_dictionary:
        value = character_dictionary[key]
        character_sort.append({"character": key, "num": value})
    character_sort.sort(reverse=True, key=sort_on)
    return character_sort
