def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    return verify_word(first_string) == verify_word(second_string)


def verify_word(str):
    word = {}
    for letter in str.lower():
        if letter in word:
            word[letter] += 1
        else:
            word[letter] = 1
    return word
