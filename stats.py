def sort_on(characters):

    return characters["num"]

def get_num_words(text):

	num_words = len(text.split())
	return f"Found {num_words} total words"


def get_num_characters(text):

    characters = {}
    text = text.lower()
    for i in text:
        if i.isalpha():
            if i not in characters:
                characters.update({i: 1})
            else:
                characters[i] += 1

    sorted = []
    for i in characters.keys():
        sorted_characters = {"char": i, "num": characters[i]}
        sorted.append(sorted_characters)

    sorted.sort(reverse=True, key=sort_on)
    return sorted
    