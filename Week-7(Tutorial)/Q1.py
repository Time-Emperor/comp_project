def count_vowels_and_consonants(word):
    vowels = "aeiouAEIOU"

    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return {"vowels": vowel_count, "consonants": consonant_count}
word_input = "Hello World"
result = count_vowels_and_consonants(word_input)
print(f"Word: '{word_input}'")
print(f"Vowels: {result['vowels']}")
print(f"Consonants: {result['consonants']}")