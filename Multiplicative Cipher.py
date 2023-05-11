# multiplicative cipher
def multiplicativeCipher(message, shift):
    cipher = ""
    
    for i in range(len(message)):
        char = message[i]
        if (char.isupper()):
            cipher += chr((((ord(char) - 65) * shift) % 26) + 65)
        else:
            cipher += chr((((ord(char) - 97) * shift) % 26) + 97)
    return cipher

def k_inverse(k):
    k_inver = 0
    for i in range(26):
        if ((i * k) % 26 == 1):
            k_inver = i
            break
    return k_inver % 26


def multiplicativeDecipher(message, shift):
    shift_inverse = k_inverse(shift)

    decipher = ""
    for i in range(len(message)):
        char = message[i]
        if (char.isupper()):
            decipher += chr((((ord(char) - 65) * shift_inverse) % 26) + 65)
        else:
            decipher += chr((((ord(char) - 97) * shift_inverse) % 26) + 97)
            
    return decipher


k = 7

# gcd(k, 26) should be equal to 1
# else the multiplicative inverse does not exist for k

cipher = multiplicativeCipher("GEEKSFORGEEKS", k)
print(cipher)
decipher = multiplicativeDecipher(cipher, k)
print(decipher)