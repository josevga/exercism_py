def reverse(text):
    return "".join((text[i] for i in range(len(text)-1, -1 , -1)))
    # better solution: return text[::-1]