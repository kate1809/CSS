import math
  
key = "HACK"
  
# Encryption
def encryptMessage(msg):
    cipher = ""
  
    # track key indices
    k_indx = 0
  
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
  
    # calculate column of the matrix
    col = len(key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # add the padding character '_' in empty
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
  
    return cipher
  
# Decryption
def decryptMessage(cipher):
    msg = ""
  
    # track key indices
    k_indx = 0
  
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
  
    # calculate column of the matrix
    col = len(key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position.
    key_lst = sorted(list(key))
  
    # create an empty matrix to 
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]
  
    return msg
  
# Driver Code
msg = "Geeks for Geeks"
  
cipher = encryptMessage(msg)
print("Encrypted Message: {}".
               format(cipher))
  
print("Decryped Message: {}".
       format(decryptMessage(cipher)))





# The first line of the code imports the 'math' module.

# The second line defines a string variable 'key' which will be used as a key for encryption and decryption.

# The 'encryptMessage(msg)' function is defined which takes a string 'msg' as input and returns the encrypted message.

# The 'cipher' variable is initialized as an empty string.

# The 'k_indx' variable is initialized as 0 which will be used to track the key indices.

# The length of the message is stored in the 'msg_len' variable.

# The 'msg_lst' variable is defined which stores the message as a list.

# The 'key_lst' variable is defined which stores the key as a sorted list.

# The number of columns of the matrix is stored in the 'col' variable which is the length of the key.

# The number of rows of the matrix is stored in the 'row' variable which is calculated by dividing the message length by the number of columns and taking the ceiling value of the result.

# The number of padding characters required to fill the empty cells of the matrix is calculated and stored in the 'fill_null' variable.

# The padding characters are added to the end of the 'msg_lst' list.

# The matrix is created by dividing the 'msg_lst' list into 'row' number of sublists, where each sublist has 'col' number of elements.

# The columns of the matrix are read using the key and the corresponding characters from each row are appended to the 'cipher' variable.

# The 'k_indx' variable is incremented by 1 and the above step is repeated for all columns.

# The encrypted message is returned.

# The 'decryptMessage(cipher)' function is defined which takes the encrypted message as input and returns the decrypted message.

# The 'msg' variable is initialized as an empty string.

# The 'k_indx' and 'msg_indx' variables are initialized as 0 which will be used to track the key and message indices respectively.

# The length of the cipher is stored in the 'msg_len' variable.

# The 'msg_lst' variable is defined which stores the cipher as a list.

# The number of columns of the matrix is stored in the 'col' variable which is the length of the key.

# The number of rows of the matrix is stored in the 'row' variable which is calculated by dividing the cipher length by the number of columns and taking the ceiling value of the result.

# The 'key_lst' variable is defined which stores the key as a sorted list.

# An empty matrix 'dec_cipher' is created to store the deciphered message.

# The columns of the matrix are arranged column-wise according to the permutation order by adding into the new matrix.

# The 'k_indx' variable is incremented by 1 and the above step is repeated for all columns.

# The decrypted message is obtained by converting the 'dec_cipher' matrix into a string.

# If there are any padding characters in the decrypted message, they are removed.

# The decrypted message is returned.

# The 'msg' variable is initialized with the original message.

# The 'cipher' variable is obtained by encrypting the original message using the 'encryptMessage(msg)' function.

# The encrypted message is printed.

# The decrypted message is obtained by decrypting the encrypted message using the 'decryptMessage(cipher)' function.

# The decrypted message is printed.