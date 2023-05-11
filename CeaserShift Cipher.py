def encrypt(plaintext,key):
    space = " "
    encrypted_text = ""
    for char in plaintext:
        if(char == space):
            encrypted_text+=" "
        elif(char.isupper()):
            encrypted_text += chr(((ord(char)-65+key)%26) + 65)
        elif(char.islower()):
            encrypted_text += chr(((ord(char)-97+key)%26) + 97)
        else:
            return("Error: Non Alphabet")
    return(encrypted_text)

def decrypt(encrypted_text,key):
    space = " "
    decrypted_text = ""
    for char in encrypted_text:
        if(char == space):
            decrypted_text+=" "
        elif(char.isupper()):
            decrypted_text += chr(((ord(char)-65-key)%26) + 65)
        elif(char.islower()):
            decrypted_text += chr(((ord(char)-97-key)%26) + 97)
        else:
            return("Error: Non Alphabet")
    return(decrypted_text)

plaintext = str(input("Enter a text: "))
key = int(input("Enter a key: "))
encrypted_text = encrypt(plaintext,key)
print("Encryped Text is: " + encrypted_text)
decrypted_text = decrypt(encrypted_text,key)
print("Decryped Text is: " + decrypted_text)
