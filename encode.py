import random

class Encode:
    def __init__(self, plainText : str = ""):
        self.__plainText = plainText
        self.__array = []


    def encodeText(self):
        self.cesar()
        return self.__array


    def cesar(self):
        dis = random.randint(1, 10) # Genera un número entre 1 y 10 que serán los desplazamientos
        codedText = ""
        for i in range(len(self.__plainText)):
            char = self.__plainText[i] # Tomamos el caracter i

            if ord(char) + dis > 126: # Comprueba limite de ASCII para evitar errores (~)
                char = chr(ord(char) - 95) # El desplazamiento llegará por el límite inferior

            char = chr(ord(char) + dis) # Convierte el caracter a ascii, realiza el desplazamiento y lo regresa a caracter
            codedText = codedText + char
            
        self.__array.append(codedText) # Agrega el texto cifrado al arreglo
        self.__array.append(str(dis)) # Agrega el displazamiento al arreglo (Como la key)


    def xor(self):
        print("")
