def cesar_cipher(message, step, decipher=False):
    if not decipher:
        encrypted = ''
        for char in message:
            # If ASCII is over 122 or under 65, no.
            asc = ord(char) + step
            if asc > 122:
                asc = asc - 122 + 65
            encrypted += ''.join(chr(asc))
        return encrypted

    else:
        decrypted = ''
        for char in message:
            asc = ord(char) - step
            if asc < 65:
                asc = asc + 122 - 65
            decrypted += ''.join(chr(asc))
        return decrypted
