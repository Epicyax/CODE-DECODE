import random

class Encode:
    def __init__(self, plainText : str = ""):
        self.__plainText = plainText
        self.__array = []


    def encodeText(self):
        self.cesar()
        return self.__array


    def cesar(self):
        dis = random.randint(1, 10)
        codedText = ""
        for i in range(len(self.__plainText)):
            char = self.__plainText[i]

            if ord(char) + dis > 126: # Limite de ASCII para evitar errores (~)
                char = chr(ord(char) - 95)

            char = chr(ord(char) + dis)
            codedText = codedText + char
            
        self.__array.append(codedText)
        self.__array.append(str(dis))


    def xor(self):
        print("")
