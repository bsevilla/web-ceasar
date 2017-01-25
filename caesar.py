import string
alphabet = list(string.ascii_lowercase)

def alphabet_position(letter):
        lowercase = letter.lower()
        return alphabet.index(lowercase)

def rotate_character(letter, rot):
    if letter.isalpha() == False:
        return letter
    else:
        position = alphabet_position(letter)
        rotation = (position + int(rot)) % len(alphabet)
        new_position = alphabet[rotation]
        if letter.isupper() == True:
            return new_position.upper()
        else:
            return new_position.lower()

def encrypt(text, rot):
    new_text = []
    for char in text:
        new_char = rotate_character(char, rot)
        new_text.append(new_char)
    return "".join(new_text)
