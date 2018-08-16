def rova(word):
    consonants = "bcdfhjklmnpqrstvwxyz"

    if not word:
        return ""
    elif word[0] in consonants:
        return word[0] + "o" + word[0] + rova(word[1:])
    else:
        return word[0] + rova(word[1:])    