def count_word(phrase: str) -> int:
    return phrase.count(" ") + 1 + phrase.count("-")


sentence = input("Qu'elle est ta phrase ?\nRep: ")
print(f'La phrase a {count_word(sentence)} mots.')
