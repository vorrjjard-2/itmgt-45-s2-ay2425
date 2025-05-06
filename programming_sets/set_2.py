def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return " "
    index = alphabet.index(letter)
    new_index = (index + shift) % 26
    return alphabet[new_index]

def caesar_cipher(message, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    for c in message:
        if c == " ":
            out.append(" ")
        else:
            index = 0
            for i, letter in enumerate(alphabet):
                if letter == c:
                    index = i
                    break
            idx = (index + shift) % 26
            out.append(alphabet[idx])
    
    return ''.join(out)

def shift_by_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return " "
    index = 0
    for i, char in enumerate(alphabet):
        if char == letter:
            index = i
            break

    shift_idx = alphabet.index(shift)
    idx = (index + shift_idx) % 26
    return alphabet[idx]

def vigenere_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    key_idx = 0 

    for char in message:
        if char == " ":
            result.append(" ") 
        else:
            key_char = key[key_idx % len(key)]
            shift = alphabet.index(key_char)

            message_index = alphabet.index(char)
            new_idx = (message_index + shift) % 26
            result.append(alphabet[new_idx])
            key_idx += 1  

    return ''.join(result)

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"

    total_len = len(message)
    cols = total_len // shift
    result = []

    for i in range(cols):
        for j in range(shift):
            result.append(message[j * cols + i])

    return ''.join(result)

def scytale_decipher(ciphered, shift):
    cols = len(ciphered) // shift
    grid = [''] * shift

    idx = 0
    for col in range(cols):
        for row in range(shift):
            grid[row] += ciphered[idx]
            idx += 1

    return ''.join(grid)
    

  
