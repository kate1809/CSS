def encrypt(plaintext,key):
    encrypted_text = ""
    for i in range(0,key):
        pointer = i
        temp = ""
        while(pointer<len(plaintext)):
            temp+=(plaintext[pointer])
            #temp.append(plaintext[pointer])
            pointer+=key
        encrypted_text+=temp
    return(encrypted_text)

def decrypt(encrypted_text,key):
    decrypted_text = ""
    last_row_value = len(encrypted_text)%key
    if(last_row_value == 0):
        whole_rows = len(encrypted_text)//key
        for i in range(0,whole_rows):
            temp = ""
            pointer = i
            while(pointer<len(encrypted_text)):
                temp += (encrypted_text[pointer])
                pointer+=whole_rows
            decrypted_text +=temp
        return(decrypted_text)
    else:
        whole_rows = len(encrypted_text)//key
        for i in range(0,whole_rows):
            temp =""
            pointer = i
            last_row_value = len(encrypted_text)%key
            while(pointer<len(encrypted_text)):
                
                decrypted_text +=temp
        return(decrypted_text)




plaintext = str(input("Enter a text: "))
key = int(input("Enter a key: "))
encrypted_text = encrypt(plaintext,key)
print("Encryped Text is: " + encrypted_text)
decrypted_text = decrypt(encrypted_text,key)
print("Decryped Text is: " + decrypted_text)