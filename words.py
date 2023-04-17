words = ['ashley', 'meeran', 'sarah', 'elie']



def print_upper_words(words):
    """take an array of words and print words in upper case"""
    for word in words:
        word_upper = word.upper()
        print(word_upper)
print("result from print_upper_words")
print_upper_words(words)

def print_only_e(words):
    """take an array of words and print words starting with 'e' or 'E'"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)
print("result from print_only_e")
print_only_e(words)