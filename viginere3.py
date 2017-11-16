baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9')
print ("Cifra Viginere")
plainText = input("Mensagem a Cifrar")
key = input("Chave")
keyList = []
keyLength = 0
while keyLength < len(plainText):
    for char in key:#Adds the users entered key into a list character by character. Also makes the key the same length as plainText
        if keyLength < len(plainText):
            keyList.append(str(char))
            keyLength = keyLength + 1
completeCipherText = [] #The variable each processed letter is appended to
cipherCharIndexValue = 0#This is the value used to temporaily store the ciphertext character during the iteration
keyIncrement = 0
for plainTextChar in plainText:#iterates through the plain text
        cipherCharIndexValue = baseAlphabet.index(keyList[keyIncrement]) + baseAlphabet.index(plainTextChar)#Adds the base alphabets index value of the key and the plain text char
        while cipherCharIndexValue > 25:
            cipherCharIndexValue = cipherCharIndexValue - 26#makes the addition value under 26 as to not go out of range of base alphabet tuple
        completeCipherText.append(baseAlphabet[cipherCharIndexValue])#appends the ciphertext character to the completeCipherText variable. The character is the index of the key + index of the plainTextChar from baseAlphabet
        keyIncrement = keyIncrement + 1#Moves onto the next key
print (''.join(completeCipherText))