
file = open("testfile.txt", "r")
#Cria uma lista em que cada elemento é uma lista
content = file.readlines()
#Devolve o numero de linhas
numLines = len(content)
print('Numero de linhas:' + str(numLines))
#Catch dos dados
for i in range(numLines):
    if(i == 0):
        rows = content[i]
        print("ROWS:"+content[i])
    if (i == 1):
        cols = content[i]
        print("COLS:"+content[i])
    if (i == 2):
        alphabet = content[i]
        print("ALPHABET:"+content[i])

def matrix(key):
    matrix = []
    for e in key.upper():
        if e not in matrix:
            matrix.append(e)


    for e in alphabet:
        if e not in matrix:
            matrix.append(e)

    # initialize a new list. Is there any elegant way to do that?
    matrix_group = []
    for e in range(int(cols)):
        matrix_group.append('')

    # Break it into 5*5
    for i in range(int(cols)):
        matrix_group[i] = matrix[(int(rows)) * i:(int(rows)) * (i + 1)]
    return matrix_group


def message_to_digraphs(message_original):
    # Change it to Array. Because I want used insert() method
    message = []
    for e in message_original:
        message.append(e)

    # Delet space
    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")

    # If both letters are the same, add an "X" after the first letter.
    i = 0
    for e in range (int(len(message) / 2)):
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i = i + 2

    # If it is odd digit, add an "X" at the end
    if len(message) % 2 == 1:
        message.append("X")
    # Grouping
    i = 0
    new = []

    for x in range (int(len(message) / 2 + 1)):
        new.append(message[i:i + 2])
        i = i + 2
    return new


def find_position(key_matrix, letter):
    linha = coluna = 0
    for i in range(int(cols)):
        for j in range(int(rows)):
            if key_matrix[i][j] == letter:
                linha = i
                coluna = j

    return linha, coluna


def encrypt(message):
    message = message_to_digraphs(message)
    message.remove(message[len(message) - 1])
    key_matrix = matrix(key)
    #print (matrix(key))
    cipher = []
    for e in message:
        linha1, coluna1 = find_position(key_matrix, e[0])
        linha2, coluna2 = find_position(key_matrix, e[1])
        print("linha1:" + str(linha1))
        print("coluna1:" + str(coluna1))
        print("linha2:" + str(linha2))
        print("coluna2:" + str(coluna2))
        if linha1 == linha2:
            bora = True
            if coluna1 == (int(rows) - 1):
                coluna1 = 0
                cipher.append(key_matrix[linha1][coluna1])
                cipher.append(key_matrix[linha2][coluna2 + 1])
                print("1:"+str(cipher))
                bora = False
            if coluna2 == (int(rows) - 1):
                coluna2 = 0
                cipher.append(key_matrix[linha1][coluna1 + 1])
                cipher.append(key_matrix[linha2][coluna2])
                print("2:" + str(cipher))
                bora = False
            elif bora == True:
                cipher.append(key_matrix[linha1][coluna1 + 1])
                cipher.append(key_matrix[linha1][coluna2 + 1])
                print("3:" + str(cipher))
        elif coluna1 == coluna2:
            bora = True
            if linha1 == int(cols) - 1:
                linha1 = 0
                cipher.append(key_matrix[linha1][coluna1])
                cipher.append(key_matrix[linha2 + 1][coluna2])
                print("4:" + str(cipher))
                bora = False
            if linha2 == int(cols) - 1:
                linha2 = 0
                cipher.append(key_matrix[linha1 + 1][coluna1])
                cipher.append(key_matrix[linha2][coluna2])
                print("5:" + str(cipher))
                bora = False
            elif bora:
                cipher.append(key_matrix[linha1 + 1][coluna1])
                cipher.append(key_matrix[linha2 + 1][coluna2])
                print("6:" + str(cipher))
        elif coluna1 != coluna2 and linha1 != linha2:
            cipher.append(key_matrix[linha1][coluna2])
            cipher.append(key_matrix[linha2][coluna1])
            print("7:" + str(cipher))
        bora = True
        print(e)
    return cipher


def cipher_to_digraphs(cipher):
    i = 0
    new = []
    for x in range(int(len(cipher) / 2)):
        new.append(cipher[i:i + 2])
        i = i + 2
    return new


def decrypt(cipher):
    cipher = cipher_to_digraphs(cipher)
    key_matrix = matrix(key)
    print(cipher)
    plaintext = []
    for e in cipher:
        linha1, coluna1 = find_position(key_matrix, e[0])
        linha2, coluna2 = find_position(key_matrix, e[1])
        if linha1 == linha2:
            if coluna1 == int(cols):
                coluna1 = 0
            if coluna2 == int(cols):
                coluna2 = 0
            plaintext.append(key_matrix[linha1][coluna1 - 1])
            plaintext.append(key_matrix[linha1][coluna2 - 1])
        elif coluna1 == coluna2:
            if linha1 == int(rows):
                linha1 = 0
            if linha2 == int(rows):
                linha2 = 0
            plaintext.append(key_matrix[linha1 - 1][coluna1])
            plaintext.append(key_matrix[linha2 - 1][coluna2])
        else:
            plaintext.append(key_matrix[linha1][coluna2])
            plaintext.append(key_matrix[linha2][coluna1])

    for unused in range(len(plaintext)):
        if "X" in plaintext:
            plaintext.remove("X")

    output = ""
    for e in plaintext:
        output += e
    return output.lower()


#app.go()
print ("Playfair Cipher")
order=input("Choose :\n1,Encrypting \n2,Decrypting\n")
if order == "1":
	key= input("Please input the key : ")
	message= input("Please input the message : ").upper()
	print ("Encrypting: \n"+"Message: "+message)
	print ("Break the message into digraphs: ")
	print (message_to_digraphs(message))
	print ("Matrix: ")
	print (matrix(key))
	print ("Cipher: " )
	print (encrypt(message))
elif order == "2":
	key= input("Please input the key : ")
	cipher= input("Please input the cipher text: ")
	#cipher="ILSYQFBWBMLIAFFQ"
	print ("\nDecrypting: \n"+"Cipher: "+cipher)
	print ("Plaintext:")
	print (decrypt(cipher.upper()))
else:
	print ("Error")

