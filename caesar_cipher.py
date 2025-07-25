def caesar_cipher(message, shift, mode='encode'):
    shift = shift % 26
    if mode == 'decode':
        shift = -shift
    result = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)
    
msg = "Agetware Tech"
shift = 4
print("Encoded:", caesar_cipher(msg, shift))
print("Decoded:", caesar_cipher(caesar_cipher(msg, shift), shift, 'decode'))