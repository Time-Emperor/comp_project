def is_palindrome(word):
    clean_word = word.lower()
    if clean_word == clean_word[::-1]:
        return True
    else:
        return False