import random
from secrets import token_bytes

class Encode:
    def __init__(self, plainText : str = ""):
        self.__plainText = plainText
        self.__array = []


    def encodeText(self):
        self.cesar()
        self.xor()
        return self.__array


    def cesar(self):
        dis = random.randint(2, 9) # Genera un número entre 2 y 9 que serán los desplazamientos
        codedText = ""
        for i in range(len(self.__plainText)):
            char = self.__plainText[i] # Tomamos el caracter i

            if ord(char) + dis > 126: # Comprueba limite de ASCII para evitar errores (~)
                    char = chr(ord(char) - 95) # El desplazamiento llegará por el límite inferior

            char = chr(ord(char) + dis) # Convierte el caracter a ascii, realiza el desplazamiento y lo regresa a caracter
            codedText = codedText + char
            
        self.__array.append(codedText) # Agrega el texto cifrado al arreglo
        self.__array.append(str(dis)) # Agrega el displazamiento al arreglo (Como la key)

    def generateKey(self):
        k = random.randint(33,126)
        return chr(k)


    def xor(self):
        cesarKey = self.__array[1]
        cesarText = self.__array[0]
        codedText = ""
        key = ""
        st = ""

        for i in range(len(self.__plainText)):
            key = key + chr(random.randint(48,96)) # Para cada caracter del texto, se crea un número del 1 al 9 que será la key
            st = chr(ord(cesarText[i]) ^ ord(key[i])) # Hace la operación xor con el ascii de cada caracter de la cadena y la key y se guarda como caracter
            codedText = codedText + st

        self.__array.clear()
        self.__array.append(codedText)
        self.__array.append(key + cesarKey)

