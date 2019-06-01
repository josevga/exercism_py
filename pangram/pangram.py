def is_pangram(sentence):
    if not sentence:
        return False
    else:
        sentence = sentence.lower()
    letters = (chr(n) for n in range(ord("a"), ord("z") + 1))
    return all(l in sentence for l in letters)
